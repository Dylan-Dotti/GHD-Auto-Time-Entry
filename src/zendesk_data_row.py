
class ZendeskDataRow:

    def __init__(self, wbs, ticket_id, update_date, minutes) -> None:
        self.wbs = wbs
        self.ticket_id = ticket_id
        self.update_date = update_date
        self.minutes = minutes