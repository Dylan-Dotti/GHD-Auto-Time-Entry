from app.auto_gui.keyboard_controller import KeyboardController
from app.interfaces.stoppable import Stoppable


class SapConfirmatPromptWindowNavigator(Stoppable):

    def __init__(self, window_kc: KeyboardController) -> None:
        self._kc = window_kc
        self._selected = False
    
    def select_yes(self):
        if not self._selected:
            self._flip_selection()
        self._kc.press_enter()
    
    def select_no(self):
        if self._selected:
            self._flip_selection()
        self._kc.press_enter()
    
    def _flip_selection(self):
        self._kc.press_tab()
        self._selected = not self._selected