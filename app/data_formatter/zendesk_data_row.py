from datetime import datetime

class ZendeskDataRow:
    '''
        zendesk_excel_row by index:
        0: the user
        2: wbs element
        5: ticket number
        7: date as a datetime
        8: time in min
    '''
    def __init__(self, row) -> None:
        
        try:
            # format date so it is readable
            d = datetime.strptime(row[7], '%Y-%m-%d').date()
            self.update_date = d

        except Exception as err:
            print(f"failed to convert date with error: {err}")
            exit(0)

        self.updater_name = row[0]
        self.wbs = row[2] or "S-003422.01.02.01"
        self.ticket_id = row[5]
        self.minutes = row[8] or 0 
