
class ZendeskDataRow:
    '''
        zendesk_excel_row by index:
        0: the user
        2: wbs element
        5: ticket number
        7: date
        8: time in min
    '''
    def __init__(self, row) -> None:
        self.updater_name = row[0]
        self.wbs = row[2]
        self.ticket_id = row[5]
        self.update_date = row[7]
        self.minutes = row[8]