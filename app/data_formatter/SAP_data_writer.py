from typing import List
from app.data_formatter.sap_data_row import SapDataRow
from app.data_formatter.SAP_Page import SapDataPage
from collections import defaultdict
from datetime import date

class SAPDataWriter:
    def __init__(self, zd_data) -> None:
        self.zd_data = zd_data
        self.collector_container = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict, {"time": [], "tickets":[]}))))
        self.merge_rows = []
    '''
      requirements:
      1. need to 
    '''
    def merge_wbs_elements(self) -> None:
        # user, wbs_element, date: {time:[], tickets:[]} time and tickets being corresponding index        
        for row in self.zd_data:
            self.collector_container[row.updater_name][row.wbs][row.update_date]["time"].append(row.minutes)
            self.collector_container[row.updater_name][row.wbs][row.update_date]["tickets"].append(row.tickets)

    '''
      join ticket ids 
      iterate ticketid list, count chars
      when hit 40, go to previous index
      create new merge object from prev index to that one for minutes and tickets
    '''
    def create_merge_rows(self):
        for user in self.collector_container.keys():
            for element in self.collector_container[user].keys():
                
                for wk_date in self.collector_container[user][element].keys():
                    item = self.collector_container[user][element][wk_date]
                    
                    tickets, times = self.create_slices(item)
                    self.merge_rows.append(MergeRow(user, element, wk_date, tickets, times))

    '''
      return all pages 
    '''
    def write_all_pages(self) -> List[SapDataRow]:
        return [SapDataRow()]

    def create_pages(self) -> List[SapDataPage]:
        return [SapDataPage(start, end) for start, end in self.get_sap_date_ranges(date.today().month)]

    def create_sap_rows(self) -> None:
        page_groups = []
        for start, end in self.get_sap_date_ranges(date.today().month):
            new_page_group = []
            for row in self.merge_rows:
                if start <= row.data <= end:
                    new_page_group.append(row)
            page_groups.append(new_page_group)

        for group in page_groups:
            # here we go through and create the actual rows?
            '''
            here we know that each of these merge rows belong here
            we know that each row is a unique date unless it is a split ticket id one
            
            '''   
            row_container = {}
            while len(group):
                merge_row = group.pop()

    '''
    '''
    def create_slices(self, item):
        count = 0 # char counter
        ticket_slices = []
        time_slices = []

        curr_time = []
        curr_ticket = []

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

        if len(curr_ticket) and len(curr_time):
            ticket_slices.append(curr_ticket)
            time_slices.append(curr_time)