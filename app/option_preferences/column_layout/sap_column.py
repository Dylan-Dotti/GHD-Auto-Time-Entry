from typing import Dict


class SapColumn:

    def __init__(self, column_name: str, enabled: bool, 
                 enabled_default: bool, default_index: int) -> None:
        self.column_name = column_name
        self.enabled = enabled
        self.enabled_default = enabled_default
        self.default_index = default_index

    def to_dict(self) -> Dict[str, any]:
        return {
            'column_name': self.column_name,
            'enabled': self.enabled,
            'enabled_default': self.enabled_default,
            'default_index': self.default_index,
        }

    @staticmethod
    def from_dict(data: Dict[str, any]) -> 'SapColumn':
        return SapColumn(
            data['column_name'], data['enabled'],
            data['enabled_default'], data['default_index'])
