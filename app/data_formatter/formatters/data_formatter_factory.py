from app.data_formatter.formatters.Zendesk_to_SAP_formatter import SAPDataFormatter

class DataFormatterFactory: 
    def __init__(self):
        pass

    def get_formatter(self, format):
        if format == "ZENDESK":
            return self.zendesk_formatter()
        print("Formatter not available")
        exit(0)

    def zendesk_formatter(self) -> SAPDataFormatter:
        return SAPDataFormatter
        
    def available_formatters(self):
        pass