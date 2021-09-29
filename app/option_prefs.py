from typing import Dict

# logical representation of the option preferences
# converts to and from dictionary for storage in option_prefs.json
class OptionPrefs:

    def __init__(self, preferred_name: str, 
                 num_sap_rows: int, use_fn_button: bool) -> None:
        self.preferred_name = preferred_name
        self.num_sap_rows = num_sap_rows
        self.use_fn_button = use_fn_button
    
    def to_dict(self) -> Dict[any]:
        return {
            'preferred_name': self.preferred_name,
            'num_sap_rows': self.num_sap_rows,
            'use_fn_button': self.use_fn_button
        }
    
    @staticmethod
    def from_dict(data: Dict[any]):
        return OptionPrefs(
            data['preferred_name'],
            data['num_sap_rows'],
            data['use_fn_button']
        )
