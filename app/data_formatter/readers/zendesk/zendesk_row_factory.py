from datetime import date, datetime
from app.data_formatter.readers.Data_Row import DataRow

# generate a row with indexes of fields
class ZendeskRowFactory:
    
    def __init__(self, header):
        try:
            self.updater_name_ind = header.index("Updater name")
            self.wbs_ind = header.index("Support WBS Element")
            self.ticket_id_ind = header.index("Ticket ID")
            self.data_ind = header.index("Update - Date")
            self.minutes_ind = header.index("Ticket Handling Time")

        except ValueError as err:
            raise RuntimeError(f"One of the required header fields is not present in the input spreadsheet.\n Please make sure the header contains the following fields: Updater name, Support WBS Element, Ticket ID, Update - Date, Ticket Handling Time") from err

    def __format_date(self, input_date) -> date:
        try:
            # format date so it is readable
            return datetime.strptime(input_date, '%Y-%m-%d').date()

        except Exception as err:
            raise RuntimeError(f"failed to convert date in spreadsheet with error: Date must be in format YYYY-mm-dd") from err

    def create_row(self, row_data):
        updater = row_data[self.updater_name_ind]
        wbs = row_data[self.wbs_ind]
        ticket_id = row_data[self.ticket_id_ind]
        up_date = self.__format_date(row_data[self.data_ind])
        minutes = row_data[self.minutes_ind]
        return DataRow(updater, wbs, ticket_id, up_date, minutes)
