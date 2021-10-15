from typing import Dict


class SapColumn:

    def __init__(self, column_name: str,
                 visible: bool, interactable: bool) -> None:
        self.column_name = column_name
        self.visible = visible
        self.interactable = interactable

    def to_dict(self) -> Dict[str, any]:
        return {
            'column_name': self.column_name,
            'visible': self.visible,
            'interactable': self.interactable,
        }

    @staticmethod
    def from_dict(data: Dict[str, any]) -> 'SapColumn':
        return SapColumn(
            data['column_name'],
            data['visible'],
            data['interactable']
        )
