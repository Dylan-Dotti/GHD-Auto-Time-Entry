import app.option_preferences.column_layout.column_names as cnames
from app.option_preferences.column_layout.default_column_layout import DEFAULT_COLUMN_LAYOUT
from app.option_preferences.column_layout.sap_column import SapColumn
from typing import Dict, List


class SapColumnLayout:

    def __init__(self, columns: List[SapColumn]) -> None:
        self.set_layout(columns)
    
    def set_layout(self, columns: List[SapColumn]) -> None:
        self._columns = columns
    
    def get_column_list(self) -> List[SapColumn]:
        return self._columns
    
    def get_column_name_list(self) -> List[str]:
        return [c.column_name for c in self._columns]
    
    def get_day_column_name_list(self) -> List[str]:
        return [cnames.MONDAY, cnames.TUESDAY, cnames.WEDNESDAY,
                cnames.THURSDAY, cnames.FRIDAY, cnames.SATURDAY, cnames.SUNDAY]
    
    # return a list of day indexes representing the order of days
    # ex: [6, 1, 4] is Sunday, Tuesday, Friday
    def get_day_relative_index_list(self) -> List[int]:
        day_names = self.get_day_column_name_list()
        column_days_list = list(filter(lambda c: c in day_names, self.get_column_name_list()))
        return [day_names.index(c) for c in column_days_list]
    
    def get_day_absolute_index_map(self) -> Dict[str, int]:
        col_names = self.get_column_name_list()
        day_names = self.get_day_column_name_list()
        return {day: col_names.index(day) for day in day_names}

    def get_visible_columns(self) -> List[SapColumn]:
        return list(filter(lambda c: c.visible, self._columns))
    
    def get_interactable_columns(self) -> List[SapColumn]:
        return list(filter(lambda c: c.interactable, self._columns))
    
    def get_visible_interactable_columns(self) -> List[SapColumn]:
        return list(filter(lambda c: c.visible and c.interactable, self._columns))
    
    def to_json_data(self) -> List[Dict[str, any]]:
        return [c.to_dict() for c in self._columns]


    @staticmethod
    def from_default_layout() -> 'SapColumnLayout':
        return SapColumnLayout(DEFAULT_COLUMN_LAYOUT)

    @staticmethod
    def from_json_data(data: List[Dict[str, any]]) -> 'SapColumnLayout':
        return SapColumnLayout([SapColumn.from_dict(c) for c in data])