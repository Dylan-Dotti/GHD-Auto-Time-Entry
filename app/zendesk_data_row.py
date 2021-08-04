
class ZendeskDataRow:

    def __init__(self, updater_name, wbs, ticket_id, update_date, minutes) -> None:
        self.updater_name = updater_name
        self.wbs = wbs
        self.ticket_id = ticket_id
        self.update_date = update_date
        self.minutes = minutes