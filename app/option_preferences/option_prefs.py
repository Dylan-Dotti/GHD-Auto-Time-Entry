from typing import Dict
from app.column_layout.sap_column_layout import SapColumnLayout

# logical representation of the option preferences
# converts to and from dictionary for storage in option_prefs.json
class OptionPrefs:

    def __init__(self, data_directory: str, name: str, 
                 num_sap_rows: int, use_fn_button: bool,
                 column_layout: SapColumnLayout) -> None:
        self.data_directory = data_directory
        self.name = name
        self.num_sap_rows = num_sap_rows
        self.use_fn_button = use_fn_button
        self.column_layout = column_layout
    
    def to_dict(self) -> Dict[str, any]:
        return {
            'data_directory': self.data_directory,
            'name': self.name,
            'num_sap_rows': self.num_sap_rows,
            'use_fn_button': self.use_fn_button,
            'column_layout': self.column_layout.to_json_data()
        }
    
    @staticmethod
    def from_dict(data: Dict[str, any]):
        return OptionPrefs(
            data['data_directory'],
            data['name'],
            data['num_sap_rows'],
            data['use_fn_button'],
            SapColumnLayout.from_json_data(data['column_layout'])
        )
