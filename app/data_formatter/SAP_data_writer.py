from typing import Counter, List
from app.data_formatter.sap_data_row import MergeRow, SapDataPage, SapDataRow
from collections import defaultdict
from datetime import date, timedelta

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

    def create_sap_pages(self) -> None:
        self.pages = [SapDataPage(start, end) for start, end in self.get_sap_date_ranges(date.today().month)]

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


    '''
      if first monday is not the first, go back a week to get first monday
      get corresponding sunday
    '''
    def get_sap_date_ranges(month):
        year = date.today().year
        d = date(year, month, 7)
        offset = -d.weekday() #weekday = 0 means monday
        d = d + timedelta(offset)

        if d.day != 1:
            # if it isn't the first of the month, go 7 days back
            d = d - timedelta(days=7)
        
        while d.month == month or d.month + 1 == month:
            yield d, (d + timedelta(days=6))
            d += timedelta(days=7)