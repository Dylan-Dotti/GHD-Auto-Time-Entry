from typing import Dict


class SapColumn:

    def __init__(self, column_name: str, visible: bool, 
                 visible_default: bool, interactable: bool, 
                 noninteractable_str: str, default_index: int) -> None:
        self.column_name = column_name
        self.visible = visible
        self.visible_default = visible_default
        self.interactable = interactable
        self.noninteractable_str = noninteractable_str
        self.default_index = default_index

    def to_dict(self) -> Dict[str, any]:
        return {
            'column_name': self.column_name,
            'visible': self.visible,
            'visible_default': self.visible_default,
            'interactable': self.interactable,
            'noninteractable_str': self.noninteractable_str,
            'default_index': self.default_index,
        }

    @staticmethod
    def from_dict(data: Dict[str, any]) -> 'SapColumn':
        return SapColumn(
            data['column_name'], data['visible'],
            data['visible_default'], data['interactable'],
            data['noninteractable_str'], data['default_index'])
