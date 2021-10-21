from app.data_formatter.SAP_Objects.sap_data_row import SapDataRow

# This is the set of rows for a monday-sunday SAP range
class SapDataPage:
    # Params:
    #   startDate - the page start date (Monday)
    #   endDate - the page end date (Sunday)
    def __init__(self, startDate, endDate) -> None:
        self.startDate = startDate
        self.endDate = endDate
        self.data = [] # order doesn't matter here

    def add_row(self, row: SapDataRow) -> None:
        self.data.append(row)