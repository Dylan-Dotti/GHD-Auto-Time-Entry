from app.data_formatter.formatters.data_formatter import DataFormatter
from typing import Any, List
from datetime import datetime
from collections import defaultdict
from app.data_formatter.readers.zendesk.zendesk_data_row import ZendeskDataRow

from app.data_formatter.SAP_Objects.sap_data_row import SapDataRow, DateEntry
from app.data_formatter.SAP_Objects.SAP_Page import SapDataPage

class MergeRow:

    # Params:
    # user    - the user
    # wbs     - the wbs element
    # date    - the date of the as a datetime
    # tickets - tickets, as a list of the ticketIds
    # times   - list of the time spent on the tickets, in minutes
    def __init__(self, user: str, wbs: str, date: datetime, tickets, times) -> None:
        self.user = user
        self.wbs = wbs
        self.date = date
        self.tickets = tickets
        self.time = times 

'''
  this is the object which converts zendesk rows to SAP Page rows. 

  parameters:
  zd_data: a list of Zendesk Rows

  methods:

'''
class SAPDataFormatter(DataFormatter):

    # Params:
    #  zd_data - a list of zendesk rows
    #  pages   - a list of SAP page objects
    def __init__(self, username: str, zd_data: List[ZendeskDataRow], pages: List[SapDataPage]) -> None:
        self.collector_container = self.__merge_wbs_elements(zd_data)
        self.pages = pages
        self.username = username
    '''
      this is for aggregating ticketIds for a wbs element, and summing up the time
    '''
    def __merge_wbs_elements(self, zd_data) -> Any:

        # user, wbs_element, date: {time:[], tickets:[]} time and tickets being corresponding index
        collector_container = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict, {"time": [], "tickets":[]}))))

        for row in zd_data:
            collector_container[row.updater_name][row.wbs][row.update_date]["time"].append(row.minutes)
            collector_container[row.updater_name][row.wbs][row.update_date]["tickets"].append(row.ticket_id)

        return collector_container

    '''
    TODO: think about this, not an ideal solution.
      process:
        1. join all ticketIds
        2. iterate ticket list, count chars
        3. when hit 40, go to previous index
        4. create new merge object from prev index to that one for minutes and tickets
    '''
    def __create_merge_rows(self):
        return_rows = []
        for user in self.collector_container.keys():
            # because of design choices this is the easiest spot to remove unnecessary users.
            if user == self.username:
                for element in self.collector_container[user].keys():
                    
                    for wk_date in self.collector_container[user][element].keys():
                        item = self.collector_container[user][element][wk_date]

                        tickets, times = self.__create_merge_slices(item)
                        for tk, ti in zip(tickets, times):
                            tickets_str = ",".join(list(tk))
                            time_sum = sum(ti)
                            if time_sum >= 1:
                                # the issue here is we're creating a new element instance for each date, when we don't care about that..
                                return_rows.append(MergeRow(user, element, wk_date, tickets_str, time_sum))
        return return_rows

    '''
      This is used to cut the ticketId's into > 40 chars so they fit into the description text field
      
      Params:
      item - this is a merge row 

      process:
        1. iterate tickets and times of a merge row 
        2. count ticket chars
        3. if it goes over and equal to 40
            1. append slices
            2. reset current tickets
            3. append times
            4. reset current times
            5. reset count
        4. if there are anything in the curr lists
        5. append to to totals
        6. return tickets and times 
    '''
    def __create_merge_slices(self, item):
        count = 0 # char counter

        # these are the totals 
        ticket_slices = []
        time_slices = []

        # this is the current one being created
        curr_time = []
        curr_ticket = set()
        
        # iterate over tickets and time. 
        for ticket, time in zip(item["tickets"], item["time"]):

            # don't add to the count if that ticket is already in there
            if ticket not in curr_ticket:
                count += len(ticket) 

            # if the count is greater than or equal to 40:
            '''
                1. add the collected ticket set to the list of sets of tickets
                2. create a new set for collecting tickets
                3. add the collected time to the list of lists of times (corresponding to tickets)
                4. create a new list for time
                5. set the char count to 0
            '''
            if count >= 40: # this should also allow the commas to be added since it will drop the last ticket id, we'll have 5 chars for commas
                ticket_slices.append(curr_ticket)
                curr_ticket = set()

                time_slices.append(curr_time)
                curr_time = []
                count = 0

            # add the ticket and time to their respective set/list
            curr_ticket.add(ticket)    
            curr_time.append(time)

        # append the current one that wasn't added.
        '''
            if there are any tickets and times in the current collectors:
            1. add them to the totals 
        '''
        if len(curr_ticket) and len(curr_time):
            ticket_slices.append(curr_ticket)
            time_slices.append(curr_time)

        # return both the tickets and the times, should have equal length
        return ticket_slices, time_slices

    '''
      process:
      1. iterate over all of the merge rows
      2. iterate over the pages
      3. if there is a row in the page for the wbs number:
         1. if the date is not on this wbs row:
         2. add that date to the row
         3. else if it does exist for that date:
           1. create new SAP row and add that date
           2. add row to page
    '''
    def __merge_to_sap(self, pages, merge_rows) -> List[SapDataPage]:

        # iterate over all of the merge rows
        while merge_rows:

            # get one merge_row
            merge_row = merge_rows.pop()

            # iterate over the pages, this is used to determine what page the merge row belongs to.
            for page in pages:
                # bool for whether or not a new entry was created. If a new entry was not created then create a new row.
                created_entry = False

                # check if the merge row belongs to this page by checking if it's create data is inside the page date range
                if page.startDate <= merge_row.date <= page.endDate:
                    # go over the existing rows in the pages data to check if one for the wbs element exists
                    for sap_row in page.data:
                        # check if the wbs element already exists on this page
                        if sap_row.wbs == merge_row.wbs:

                            '''
                              check if there is a dat entry on this date, if there is 
                              then break out and create new row. This is done because this would
                              only heppen if the ticket string is longer than 40 characters and
                              multiple instances were created.
                            '''
                            if sap_row.date_entries[merge_row.date.weekday()]: 
                                break
                            
                            # if the row exists and the date is not already taken, add entry to this row.
                            new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                            sap_row.add_time(new_entry)
                            created_entry = True
                            break
                    
                    '''
                      if an entry was not created because:
                        -  the wbs element does not exist
                        -  the date collided with an existing entry

                        1. create a new row
                        2. create a new date entry 
                        3. add the date entry to the row and add the row to the respective page
                        4. break out since this is the correct page to be in
                    '''
                    if not created_entry:
                        new_row = SapDataRow("10000", merge_row.wbs, "H", page.startDate, page.endDate)
                        new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                        new_row.add_time(new_entry)
                        page.add_row(new_row)
                        break

        # here return data as SAP pages here
        return pages

    def format(self):
        merge_rows = self.__create_merge_rows()

        # fill the pages with the merge rows
        complete_sap_pages = self.__merge_to_sap(self.pages, merge_rows)
        
        self.cleaned_data = complete_sap_pages

