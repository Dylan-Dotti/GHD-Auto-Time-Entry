import app.auto_gui.keyboard_controller as kc

# Handles the controlling of the cell details window where notes are added
class SapDetailsWindowNavigator:

    def __init__(self) -> None:
        pass

    def cancel_and_close(self):
        kc.press_esc(post_delay=1)
    
    def confirm_and_close(self):
        kc.press_enter(post_delay=1)
    
    def move_to_short_text_field(self):
        kc.press_tab(num_times=4, post_delay=0.25)
