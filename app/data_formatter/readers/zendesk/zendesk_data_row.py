from datetime import datetime

# generate a row with indexes of fields
class ZendeskRowFactory:
    def __init__(self, header):
        self.updater_name_ind = header.index("Updater name")
        self.wbs_ind = header.index("Support WBS Element")
        self.ticket_id_ind = header.index("Ticket ID")
        self.data_ind = header.index("Update - Date")
        self.minutes_ind = header.index("Ticket Handling Time")

    def create_row(self, row_data):
        updater = row_data[self.updater_name_ind]
        wbs = row_data[self.wbs_ind]
        ticket_id = row_data[self.ticket_id_ind]
        up_date = row_data[self.data_ind]
        minutes = row_data[self.minutes_ind]
        return ZendeskDataRow(updater, wbs, ticket_id, up_date, minutes)

class ZendeskDataRow:
    '''
        zendesk_excel_row by index:
        0: the user
        2: wbs element
        5: ticket number
        7: date as a datetime
        8: time in min
    '''
    def __init__(self, updater, wbs, ticketId, update_date, minutes) -> None:
        
        try:
            # format date so it is readable
            d = datetime.strptime(update_date, '%Y-%m-%d').date()
            self.update_date = d

        except Exception as err:
            print(f"failed to convert date with error: {err}")
            exit(0)

        self.updater_name = updater
        self.wbs = wbs or "S-003422.01.02.01"
        self.ticket_id = ticketId
        self.minutes = minutes or 0 
    
    def __str__(self) -> str:
        return ('ZendeskDataRow(user: %s, wbs: %s, ticket: %s, date: %s, minutes: %s)' %
                (self.updater_name, self.wbs, self.ticket_id, self.update_date, self.minutes))
