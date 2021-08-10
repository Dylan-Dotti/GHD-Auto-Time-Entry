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

    def __init__(self, user: str, wbs: str, date: datetime, tickets, times) -> None:
        self.user = user
        self.wbs = wbs
        self.date = date
        self.tickets = ",".join(tickets)
        self.time = sum(times)

class DataFormatter:
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
                        self.merge_rows.append(MergeRow(user, element, wk_date, tk, ti))


    '''
      This is used to cut the ticketId's into > 40 chars so they fit into the description text field
      process:
        1. 
    '''
    def create_merge_slices(self, item):
        count = 0 # char counter

        # these are the totals 
        ticket_slices = []
        time_slices = []

        # this is the current one being created
        curr_time = []
        curr_ticket = []
        
        # iterate over tickets and time. 
        for ticket, time in zip(item["tickets"], item["time"]):
            count += len(ticket)
    
            if count >= 40:
                ticket_slices.append(curr_ticket)
                curr_ticket = []

                time_slices.append(curr_time)
                curr_time = []
                count = 0

            curr_ticket.append(ticket)    
            curr_time.append(time)

        # append the current one that wasn't added.
        if len(curr_ticket) and len(curr_time):
            ticket_slices.append(curr_ticket)
            time_slices.append(curr_time)

        return ticket_slices, time_slices


    '''
      create pages
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
        pages = self.create_pages()
        
        # iterate over all of the marge rows
        while self.merge_rows:

            # get one
            merge_row = self.merge_rows.pop()

            # iterate over the pages
            for page in pages:
                
                # to create new row or not
                is_new_row = False

                # if the merge row belongs to this page
                if page.startDate <= merge_row.date <= page.endDate:
                  
                    # iterate over the sap rows in this page
                    if page.data:
                        for sap_row in page.data:

                            # if the wbs element already exists on this page
                            if sap_row.wbs == merge_row.wbs:
                            
                                if sap_row.date_entries[merge_row.date.weekday()]:
                                    is_new_row = True
                                    break

                                new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                                sap_row.add_time(new_entry)

                            # if wbs element not in page 
                            else:
                                is_new_row = True
                                break
                    else:
                        is_new_row = True

                    if is_new_row:
                        # create a new row here, w/ date entry
                        new_row = SapDataRow("10000", merge_row.wbs, "m", page.startDate, page.endDate)
                        new_entry = DateEntry(str(merge_row.time), merge_row.tickets, merge_row.date)
                        new_row.add_time(new_entry)
                        page.add_row(new_row)
                        break

        # here return data
        return pages