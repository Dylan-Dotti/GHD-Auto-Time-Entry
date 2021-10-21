from app.data_formatter.formatters.Zendesk_to_SAP_formatter import SAPDataFormatter
AVAILABLE_FORMATTERS = ['ZENDESK']

class DataFormatterFactory: 
    def __init__(self):
        pass

    def get_formatter(self, format):
        if format == "ZENDESK":
            return self.zendesk_formatter()
        elif format == 'SALESFORCE':
            return self.salesforce_formatter()
            
        print("Formatter not available")
        exit(0)

    def zendesk_formatter(self) -> SAPDataFormatter:
        return SAPDataFormatter
    
    def salesforce_formatter(Self) -> None:
        return None

    def available_formatters(self):
        return AVAILABLE_FORMATTERS