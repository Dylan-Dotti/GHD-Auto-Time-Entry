from typing import List


# Contains the data that is entered on a single day of a single row
class DateEntry:

    # Params:
    #   time - total time (hours or minutes) for the day from the tickets listed in the note
    #   note - comma separated list of ticket IDS. ex: '59972, 59973, 59974'
    def __init__(self, time: str, note: str) -> None:
        self.time = time
        self.note = note
    
    def __str__(self) -> str:
        return 'DateEntry(time: %s, note: \'%s\')' % (self.time, self.note)


# Contains all the data needed for a single row of the SAP time sheet
class SapDataRow:

    # Params:
    #   act - usually 10000
    #   wbs - wbs of the site
    #   mu - H for hours or M for minutes
    #   date_entries - list of DateEntry. Order of elements represents Mon-Sun.
    def __init__(self, act: str, wbs: str, unit: str, startDate, endDate) -> None:
        self.act = act
        self.wbs = wbs
        self.unit = unit
        self.startDate = startDate
        self.endDate = endDate 
        self.date_entries = []
    
    def add_time(self, data:DateEntry) -> None:
        self.date_entries.append(data)

    def to_sap_str(self) -> str:
        sap_str = 'act	 	 	 	wbs	 	 	 		mu 	 	mon	 	 	tue	 	 	wed	 	 	thu	 	 	fri	 	 	sat	 	 	sun'
        sap_str = sap_str.replace('act', self.act)
        sap_str = sap_str.replace('wbs', self.wbs)
        sap_str = sap_str.replace('mu', self.unit)
        sap_str = sap_str.replace('mon', self.date_entries[0].time if self.date_entries[0] is not None else '')
        sap_str = sap_str.replace('tue', self.date_entries[1].time if self.date_entries[1] is not None else '')
        sap_str = sap_str.replace('wed', self.date_entries[2].time if self.date_entries[2] is not None else '')
        sap_str = sap_str.replace('thu', self.date_entries[3].time if self.date_entries[3] is not None else '')
        sap_str = sap_str.replace('fri', self.date_entries[4].time if self.date_entries[4] is not None else '')
        sap_str = sap_str.replace('sat', self.date_entries[5].time if self.date_entries[5] is not None else '')
        sap_str = sap_str.replace('sun', self.date_entries[6].time if self.date_entries[6] is not None else '')
        return sap_str

    def __str__(self) -> str:
        return ('SapDataRow(act: %s, wbs: %s, mu: %s, date_entries: %s)' %
                    (self.act, self.wbs, self.unit, 
                     [str(s) for s in self.date_entries]))

# This is the set of rows for a monday-sunday SAP range
class SapDataPage:

    def __init__(self, startDate, endDate) -> None:
        self.startDate = startDate
        self.endDate = endDate
        self.data = []

    def add_row(self, row: SapDataRow) -> None:
        self.data.append(row)

'''
  this is a temp structure similar to the zendesk row 
  but is holding the sliced ticket numbers and times for a date
'''
class MergeRow:

    def __init__(self, user: str, wbs: str, date: str, tickets, times) -> None:
        self.user = user
        self.wbs = wbs
        self.date = date
        self.tickets = ",".join(tickets)
        self.time = sum(times)