from app.auto_gui.keyboard_controller import KeyboardController

# Handles the controlling of the cell details window where notes are added
class SapDetailsWindowNavigator:

    def __init__(self, sap_details_keyboard_controller: KeyboardController) -> None:
        self._kc = sap_details_keyboard_controller

    def cancel_and_close(self):
        self._kc.press_esc(post_delay=1)
    
    def confirm_and_close(self):
        self._kc.press_enter(post_delay=1)
    
    def move_to_short_text_field(self):
        self._kc.press_tab(num_times=4, post_delay=0.25)
