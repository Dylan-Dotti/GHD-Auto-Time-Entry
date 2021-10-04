from typing import Dict

# logical representation of the option preferences
# converts to and from dictionary for storage in option_prefs.json
class OptionPrefs:

    def __init__(self, data_directory: str, name: str, 
                 num_sap_rows: int, use_fn_button: bool) -> None:
        self.data_directory = data_directory
        self.name = name
        self.num_sap_rows = num_sap_rows
        self.use_fn_button = use_fn_button
    
    def to_dict(self) -> Dict[str, any]:
        return {
            'data_directory': self.data_directory,
            'name': self.name,
            'num_sap_rows': self.num_sap_rows,
            'use_fn_button': self.use_fn_button
        }
    
    @staticmethod
    def from_dict(data: Dict[str, any]):
        return OptionPrefs(
            data['data_directory'],
            data['name'],
            data['num_sap_rows'],
            data['use_fn_button']
        )
