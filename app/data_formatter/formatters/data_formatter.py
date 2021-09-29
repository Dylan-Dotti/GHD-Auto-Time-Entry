from typing import List
from app.data_formatter.SAP_Objects.SAP_Page import SapDataPage
from app.data_formatter.utils import date_ranges

class DataFormatter:
    def __init__(self) -> None:
        self.data = List[SapDataPage]
        
    # create pages w/ date ranges
    @classmethod
    def create_pages(self, month) -> List[SapDataPage]:
        return [SapDataPage(start, end) for start, end in date_ranges(month)]

    # child class must implement
    def format(self):
        pass
    
    # return the formatted data
    def formatted_data(self) -> List[SapDataPage]:
        return self.data

    # get a specific page within a a start and end date
    def get_page(self, start, end) -> SapDataPage:
        for page in self.data:
            if page.startDate.strftime('%m/%d/%Y') == start and page.endDate.strftime('%m/%d/%Y') == end:
                return page
        return None