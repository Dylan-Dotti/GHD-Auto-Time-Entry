from typing import Dict, List
from app.option_preferences.column_layout.sap_column import SapColumn


class SapColumnLayout:

    def __init__(self, columns: List[SapColumn]) -> None:
        self._columns = columns
    
    def get_current_layout(self) -> List[SapColumn]:
        return self._columns
    
    def get_default_layout(self) -> List[SapColumn]:
        return sorted(self._columns, key=lambda c: c.default_index)
    
    def to_json_data(self) -> List[Dict[str, any]]:
        return [c.to_dict() for c in self._columns]
    
    @staticmethod
    def from_json_data(data: List[Dict[str, any]]) -> 'SapColumnLayout':
        return SapColumnLayout([SapColumn.from_dict(c) for c in data])