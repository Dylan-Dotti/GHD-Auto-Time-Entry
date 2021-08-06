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
        return 'DateEntry(time: %s, note: %s)' % (self.time, self.note)


# Contains all the data needed for a single row of the SAP time sheet
class SapDataRow:

    # Params:
    #   act - usually 10000
    #   wbs - wbs of the site
    #   mu - H for hours or M for minutes
    #   date_entries - list of DateEntry. Order of elements represents Mon-Sun.
    def __init__(self, act: str, wbs: str, unit: str,
                 date_entries: List[DateEntry]) -> None:
        self.act = act
        self.wbs = wbs
        self.unit = unit
        self.date_entries = date_entries
    
    def __str__(self) -> str:
        return ('SapDataRow(act: %s, wbs: %s, mu: %s, date_entries %s)' %
                    (self.act, self.wbs, self.unit, str(self.date_entries)))
