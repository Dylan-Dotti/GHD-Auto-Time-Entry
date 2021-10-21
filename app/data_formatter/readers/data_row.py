'''
  data row we run formatters on
'''
class DataRow:

    # Params:
    #   updater - the username for the row
    #   wbs - the wbs element for the row
    #   ticketId - the ticket id for the row
    #   update_date - the date for the row
    #   minutes - the amount of time in minutes for the row
    def __init__(self, updater, wbs, ticketId, update_date, minutes) -> None:

        self.updater_name = updater
        self.wbs = self.__set_wbs(wbs)
        self.update_date = update_date
        self.ticket_id = ticketId
        self.minutes = self.__set_minutes(minutes)
        
    # use the base number if one isn't provided.
    def __set_wbs(self, wbs) -> str:
        return wbs or "S-003422.01.02.01"

    # if no minutes set to 0
    def __set_minutes(self, minutes):
        return minutes or 0

    def __str__(self) -> str:
        return ('DataRow(user: %s, wbs: %s, ticket: %s, date: %s, minutes: %s)' %
                (self.updater_name, self.wbs, self.ticket_id, self.update_date, self.minutes))