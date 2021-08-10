from typing import List
from app.data_formatter.sap_data_row import SapDataRow, DateEntry
from app.data_formatter.SAP_Page import SapDataPage
from collections import defaultdict
from app.data_formatter.utils import date_ranges
from datetime import date, datetime

'''
  this is a temp structure similar to the zendesk row 
  but is holding the sliced ticket numbers and times for a date
'''
class MergeRow:

    # Params:
    #   user - the user
    #   wbs - the wbs element
    #   date - the date of the as a datetime
    #   tickets - tickets, as a list of the ticketIds
    #   times - list of the time spent on the tickets, in minutes
    def __init__(self, user: str, wbs: str, date: datetime, tickets, times) -> None:
        self.user = user
        self.wbs = wbs
        self.date = date
        self.tickets = ",".join(list(tickets))
        self.time = sum(times)

'''

'''
class DataFormatter:

    # Params:
    #   zd_data - a list of zendesk rows
    def __init__(self, zd_data) -> None:
        self.zd_data = zd_data
        self.collector_container = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict, {"time": [], "tickets":[]}))))
        self.merge_rows = []

    '''
      this is for aggregating ticketIds for a wbs element, and summing up the time
    '''
    def merge_wbs_elements(self) -> None:
        # user, wbs_element, date: {time:[], tickets:[]} time and tickets being corresponding index        
        for row in self.zd_data:
            self.collector_container[row.updater_name][row.wbs][row.update_date]["time"].append(row.minutes)
            self.collector_container[row.updater_name][row.wbs][row.update_date]["tickets"].append(row.ticket_id)

    '''
      process:
        1. join all ticketIds
        2. iterate ticket list, count chars
        3. when hit 40, go to previous index
        4. create new merge object from prev index to that one for minutes and tickets
    '''
    def create_merge_rows(self):
        for user in self.collector_container.keys():
            for element in self.collector_container[user].keys():
                
                for wk_date in self.collector_container[user][element].keys():
                    item = self.collector_container[user][element][wk_date]

                    tickets, times = self.create_merge_slices(item)
                    for tk, ti in zip(tickets, times):

                        # the issue here is we're creting a new element instance for each date, when we don't care about that..
                        self.merge_rows.append(MergeRow(user, element, wk_date, tk, ti))


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
    def create_merge_slices(self, item):
        count = 0 # char counter

        # these are the totals 
        ticket_slices = []
        time_slices = []

        # this is the current one being created
        curr_time = []
        curr_ticket = set()
        
        # iterate over tickets and time. 
        for ticket, time in zip(item["tickets"], item["time"]):
            if ticket not in curr_ticket:
                count += len(ticket)
    
            if count >= 40:
                ticket_slices.append(curr_ticket)
                curr_ticket = set()

                time_slices.append(curr_time)
                curr_time = []
                count = 0

            curr_ticket.add(ticket)    
            curr_time.append(time)

        # append the current one that wasn't added.
        if len(curr_ticket) and len(curr_time):
            ticket_slices.append(curr_ticket)
            time_slices.append(curr_time)

        return ticket_slices, time_slices


    '''
      create pages w/ date ranges
    '''
    def create_pages(self) -> List[SapDataPage]:
        return [SapDataPage(start, end) for start, end in date_ranges(date.today().month)]

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
    def create_sap_rows(self) -> List[SapDataPage]:

        # create pages
        pages = self.create_pages()

        # iterate over all of the merge rows
        while self.merge_rows:

            # get one merge_row
            merge_row = self.merge_rows.pop()

            # iterate over the pages
            for page in pages:
                
                # to create new row or not
                created_entry = False

                # if the merge row belongs to this page
                if page.startDate <= merge_row.date <= page.endDate:

                    # go over the existing rows in the pages data
                    for sap_row in page.data:

                        # if the wbs element already exists on this page
                        if sap_row.wbs == merge_row.wbs:
                            
                            # if there is a data entry on this date, then break out and create new row
                            if sap_row.date_entries[merge_row.date.weekday()]: 
                                break
                            
                            # add entry to this row
                            new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                            sap_row.add_time(new_entry)
                            created_entry = True
                            break
                    
                    # TODO need to create a row if one wasn't found and one wasn't added to an existing one

                    if not created_entry:
                        new_row = SapDataRow("10000", merge_row.wbs, "H", page.startDate, page.endDate)
                        new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                        new_row.add_time(new_entry)
                        page.add_row(new_row)
                        break

        # here return data
        return pages