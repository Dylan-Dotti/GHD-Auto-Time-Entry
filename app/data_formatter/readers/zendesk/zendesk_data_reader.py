from typing import Any, List
from app.data_formatter.readers.zendesk.zendesk_data_row import ZendeskDataRow, ZendeskRowFactory
from pathlib import Path 
from openpyxl import load_workbook
from app.data_formatter.utils import verify_path
from datetime import datetime

class ZendeskDataReader:

    def __init__(self, src_file_path: str, username=None) -> None:
        # escape path 
        self._src_file_path = Path(r"{input_path}".format(input_path=src_file_path))
        self.username = username
        self.data = None
        self.header = None
        self.users = None
        self.range_st = self.range_nd = None

    def load_wb(self):
        if not verify_path(self._src_file_path):
            print("Input is not a file or an excel spreadsheet.")
            exit(0)
        
        try:
            self.data = load_workbook(filename=self._src_file_path).active
            self.__get_header()
            
        except Exception as err:
            print(f"Failed to parse excel with error: {err}")
            exit(0)

    '''
      get the users on the spreadsheet to populate the dropdown
    '''
    def get_users(self):
        user_col = self.header.index("Updater name")
        self.users = list(set([dt[user_col] for dt in self.data.iter_rows(min_row=2, values_only=True)]))

    '''
      get the date range to populate the spreadsheet date range dropdown
    '''
    def get_dates(self):

        date_col = self.header.index("Update - Date")
        r = []

        for dt in self.data.iter_rows(min_row=2, values_only=True):
             d = datetime.strptime(dt[date_col], '%Y-%m-%d').date()
             r.append(d)

        self.range_st, self.range_nd = min(r), max(r)
    '''
      get the header row so we can match the fields
    '''
    def __get_header(self):
        self.header = list(next(self.data.iter_rows(min_row=1, max_row=1, values_only=True)))

    def read_all_rows(self) -> List[ZendeskDataRow]:
        zendesk_row_factory = ZendeskRowFactory(self.header)
        return [zendesk_row_factory.create_row(row) for row in self.data.iter_rows(min_row=2, values_only=True)]
