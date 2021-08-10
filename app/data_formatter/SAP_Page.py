from app.data_formatter.sap_data_row import SapDataRow

# This is the set of rows for a monday-sunday SAP range
class SapDataPage:

    def __init__(self, startDate, endDate) -> None:
        self.startDate = startDate
        self.endDate = endDate
        self.data = [] # order doesn't matter here

    def add_row(self, row: SapDataRow) -> None:
        self.data.append(row)