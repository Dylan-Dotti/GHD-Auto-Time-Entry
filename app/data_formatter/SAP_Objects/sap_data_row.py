from typing import List
import app.option_preferences.column_layout.column_names as cnames
from app.option_preferences.column_layout.sap_column_layout import SapColumnLayout
from datetime import datetime

# Contains the data that is entered on a single day of a single row
class DateEntry:

    # Params:
    #   time - total time (hours or minutes) for the day from the tickets listed in the note
    #   note - comma separated list of ticket IDS. ex: '59972, 59973, 59974'
    #   date - the date of the occurence. Will make it much easier w/ this on there
    def __init__(self, time: str, note: str, date: datetime) -> None:
        self.time = time
        self.note = note
        self.date = date

    def __str__(self) -> str:
        return 'DateEntry(time: %s, note: \'%s\', date: %s)' % (self.time, self.note, str(self.date))


# Contains all the data needed for a single row of the SAP time sheet
class SapDataRow:

    # Params:
    #   act - usually 10000.
    #   wbs - wbs of the site.
    #   mu - H for hours or M for minutes.
    #   startDate - the beginning on the week, Monday. 
    #   endDate - the end of the week, Sunday.
    def __init__(self, act: str, wbs: str, unit: str, startDate, endDate) -> None:
        self.act = self.__set_act(act)
        self.wbs = wbs
        self.unit = unit
        self.startDate = startDate
        self.endDate = endDate 
        self.date_entries: List[DateEntry] = self.__create_date_entries()
    
    # use provided act or default to 10000
    def __set_act(self, act):
        return act or '10000'

    # Order of elements represents Mon-Sun.
    def __create_date_entries(self):
        return [None] * 7

    def add_time(self, data:DateEntry) -> None:
        dow = data.date.weekday()
        if self.unit == "H":
            data.time = "{:.2f}".format(float(data.time)/60)
        self.date_entries[dow] = data

    def to_sap_str(self) -> str:
        sap_str = 'act	 	 	 	wbs	 	 	 		mu 	 	mon	 	 	tue	 	 	wed	 	 	thu	 	 	fri	 	 	sat	 	 	sun'
        sap_str = sap_str.replace('act', self.act)
        sap_str = sap_str.replace('wbs', self.wbs)
        sap_str = sap_str.replace('mu', self.unit)
        sap_str = sap_str.replace('mon', self.date_entries[0].time if self.date_entries[0] else '')
        sap_str = sap_str.replace('tue', self.date_entries[1].time if self.date_entries[1] else '')
        sap_str = sap_str.replace('wed', self.date_entries[2].time if self.date_entries[2] else '')
        sap_str = sap_str.replace('thu', self.date_entries[3].time if self.date_entries[3] else '')
        sap_str = sap_str.replace('fri', self.date_entries[4].time if self.date_entries[4] else '')
        sap_str = sap_str.replace('sat', self.date_entries[5].time if self.date_entries[5] else '')
        sap_str = sap_str.replace('sun', self.date_entries[6].time if self.date_entries[6] else '')
        return sap_str
    
    def to_sap_str_dynamic(self, column_layout: SapColumnLayout):
        # generate column strings
        col_strings = []
        for col in column_layout.get_column_list():
            if col.column_name == cnames.ACTTYP:
                col_str = self.act
            elif col.column_name == cnames.RECEIVER_WBS:
                col_str = self.wbs
            elif col.column_name == cnames.MU:
                col_str = self.unit
            elif col.column_name == cnames.MONDAY:
                col_str = self.date_entries[0].time if self.date_entries[0] else ''
            elif col.column_name == cnames.TUESDAY:
                col_str = self.date_entries[1].time if self.date_entries[1] else ''
            elif col.column_name == cnames.WEDNESDAY:
                col_str = self.date_entries[2].time if self.date_entries[2] else ''
            elif col.column_name == cnames.THURSDAY:
                col_str = self.date_entries[3].time if self.date_entries[3] else ''
            elif col.column_name == cnames.FRIDAY:
                col_str = self.date_entries[4].time if self.date_entries[4] else ''
            elif col.column_name == cnames.SATURDAY:
                col_str = self.date_entries[5].time if self.date_entries[5] else ''
            elif col.column_name == cnames.SUNDAY:
                col_str = self.date_entries[6].time if self.date_entries[6] else ''
            else:
                col_str = ''
            col_strings.append(col_str)
        # combine column strings into row
        return '\t'.join(col_strings)

    def __str__(self) -> str:
        return ('SapDataRow(act: %s, wbs: %s, mu: %s, date_entries: %s)' %
                    (self.act, self.wbs, self.unit, 
                     [str(s) for s in self.date_entries]))
    
    def __lt__(self, other):
        for entry, other_entry in zip(self.date_entries, other.date_entries):
            if entry is None and other_entry is not None:
                return False
            if entry is not None and other_entry is None:
                return True
        return False
