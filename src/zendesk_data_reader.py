from typing import List
from zendesk_data_row import ZendeskDataRow


class ZendeskDataReader:

    def __init__(self, src_file_path) -> None:
        self._src_file_path = src_file_path

    # reads data from the .xlsx file at the path provided in __init__
    # and returns all rows formatted into a list/array of ZendeskDataRow
    def read_all_rows() -> List[ZendeskDataRow]:
        return []