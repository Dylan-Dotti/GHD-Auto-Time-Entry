import app.option_preferences.column_layout.column_names as cnames
from typing import Dict, List
from app.option_preferences.column_layout.default_column_layout import DEFAULT_COLUMN_LAYOUT
from app.option_preferences.column_layout.sap_column import SapColumn


class SapColumnLayout:

    def __init__(self, columns: List[SapColumn]) -> None:
        self.set_layout(columns)
    
    def set_layout(self, columns: List[SapColumn]) -> None:
        self._columns = columns
    
    def get_column_list(self) -> List[SapColumn]:
        return self._columns
    
    def to_json_data(self) -> List[Dict[str, any]]:
        return [c.to_dict() for c in self._columns]
    
    def get_day_index_map(self) -> Dict[str, int]:
        day_names = [cnames.MONDAY, cnames.TUESDAY, cnames.WEDNESDAY,
                     cnames.THURSDAY, cnames.FRIDAY, cnames.SATURDAY, cnames.SUNDAY]
        col_names = [c.column_name for c in self._columns]
        return {day: col_names.index(day) for day in day_names}
        

    @staticmethod
    def from_default_layout() -> 'SapColumnLayout':
        return SapColumnLayout(DEFAULT_COLUMN_LAYOUT)

    @staticmethod
    def from_json_data(data: List[Dict[str, any]]) -> 'SapColumnLayout':
        return SapColumnLayout([SapColumn.from_dict(c) for c in data])