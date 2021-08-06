from typing import Any, List
from app.data_formatter.zendesk_data_row import ZendeskDataRow
from pathlib import Path 
from openpyxl import load_workbook
from app.data_formatter.utils import verify_path

class ZendeskDataReader:

    def __init__(self, src_file_path: str) -> None:
        # escape path 
        self._src_file_path = Path(r"{input_path}".format(input_path=src_file_path))
        self.data = None

    def load_wb(self):
        if not verify_path(self._src_file_path):
            print("Input is not a file or an excel spreadsheet.")
            exit(0)
        
        try:
            self.data = load_workbook(filename=self._src_file_path).active

        except Exception as err:
            print(f"Failed to parse with error: {err}")
            exit(0)

    # reads data from the .xlsx file at the path provided in __init__
    # and returns all rows formatted into a list/array of ZendeskDataRow
    def read_all_rows(self) -> List[ZendeskDataRow]:
        
        return [ZendeskDataRow(row) for row in self.data.iter_rows(min_row=2, values_only=True)]
