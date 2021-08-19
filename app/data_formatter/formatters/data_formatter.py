from typing import List
from app.data_formatter.SAP_Objects.SAP_Page import SapDataPage
from app.data_formatter.utils import date_ranges
from datetime import datetime

class DataFormatter:
    def __init__(self) -> None:
        self.cleaned_data = List[SapDataPage]
        
    '''
      create pages w/ date ranges
    '''
    @classmethod
    def create_pages(self, month) -> List[SapDataPage]:
        return [SapDataPage(start, end) for start, end in date_ranges(month)]

    def format(self):
        pass

    def formatted_data(self) -> List[SapDataPage]:
        return self.cleaned_data