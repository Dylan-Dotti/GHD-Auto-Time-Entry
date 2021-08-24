from datetime import datetime
from collections import defaultdict

'''
  requirements:
  - need to take all of the zendesk rows, and merge 
  1. iterate all zendesk rows:
    - pop a row
    - check if , user, wbs, and date exist for a row
    - if they exist, append time and ticketId
    - else create new merge row
'''
# class MergeRowCreator:
#     def __init__(self, zd_data) -> None:
#         self.zd_data = zd_data
#         self.cont = defaultdict(MergeRow)

#     def __create_merge_row(self):
#         pass
    
#     '''
#       This is to seperate a merge_row if it's too large.
#     '''
#     def __sheer(self, row):
        
#         pass

#     def create(self):
#         while self.zd_data:
#             zd_row = self.zd_data.pop()
            
#             # this is the key in the cont
#             k = f"{zd_row.updater_name}|{zd_row.wbs}|{zd_row.ticket_id}|{zd_row.update_date}"

#         pass

'''
  this is a temp structure similar to the zendesk row 
  but is holding the sliced ticket numbers and times for a date
'''
# class MergeRow:

#     # Params:
#     #   user - the user
#     #   wbs - the wbs element
#     #   date - the date of the as a datetime
#     #   tickets - tickets, as a list of the ticketIds
#     #   times - list of the time spent on the tickets, in minutes
#     def __init__(self, user: str, wbs: str, date: datetime, tickets, times) -> None:
#         self.user = user
#         self.wbs = wbs
#         self.date = date
#         self.tickets = ",".join(list(tickets))
#         self.time = sum(times)

    # used for 
    # def set_fields(self, user: str, wbs: str, date: datetime, tickets, times):
    #     self.user = user
    #     self.wbs = wbs
    #     self.date = date
    #     self.tickets = ",".join(list(tickets))
    #     self.time = sum(times)

    # def add_ticket_and_time(self, ticket, time):
    #     self.tickets.add(ticket)
    #     self.time.append(time)

    # def merge_tickets_and_time(self):
    #     self.tickets = ",".join(list(self.tickets))
    #     self.time = sum(self.time)
