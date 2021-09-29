from datetime import datetime

# generate a row with indexes of fields
class ZendeskRowFactory:
    def __init__(self, header):
        try:
            self.updater_name_ind = header.index("Updater name")
            self.wbs_ind = header.index("Support WBS Element")
            self.ticket_id_ind = header.index("Ticket ID")
            self.data_ind = header.index("Update - Date")
            self.minutes_ind = header.index("Ticket Handling Time")

        except IndexError:
            print(f"One of the required header fields is not present in the input spreadsheet.\n Please make sure the header contains the following fields: Updater name, Support WBS Element, Ticket ID, Update - Date, Ticket Handling Time")
            exit(0)

    def create_row(self, row_data):
        updater = row_data[self.updater_name_ind]
        wbs = row_data[self.wbs_ind]
        ticket_id = row_data[self.ticket_id_ind]
        up_date = row_data[self.data_ind]
        minutes = row_data[self.minutes_ind]
        return ZendeskDataRow(updater, wbs, ticket_id, up_date, minutes)

class ZendeskDataRow:

    def __init__(self, updater, wbs, ticketId, update_date, minutes) -> None:
        
        try:
            # format date so it is readable
            d = datetime.strptime(update_date, '%Y-%m-%d').date()
            self.update_date = d

        except Exception:
            print(f"failed to convert date in spreadsheet with error: Date must be in format YYYY-mm-dd")
            exit(0)

        self.updater_name = updater
        self.wbs = wbs or "S-003422.01.02.01" # use the base number if one isn't provided.
        self.ticket_id = ticketId
        self.minutes = minutes or 0 # if no minutes set to 0
    
    def __str__(self) -> str:
        return ('ZendeskDataRow(user: %s, wbs: %s, ticket: %s, date: %s, minutes: %s)' %
                (self.updater_name, self.wbs, self.ticket_id, self.update_date, self.minutes))
