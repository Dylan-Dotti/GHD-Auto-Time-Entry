
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_window_navigator import SapWindowNavigator
    import time

    wc = factory.get_sap_main_window_controller()
    wc.set_window_foreground()
    wc.wait_for_window_foreground()
    kc = KeyboardController(wc)

    nav = SapWindowNavigator(kc)
    for _ in range(5):
        nav.move_next_col()
        time.sleep(.5)
    for _ in range(5):
        nav.move_prev_col()
        time.sleep(.5)
    
    nav.move_current_row_end()
    nav.move_next_col()
    nav.move_current_row_end()
    nav.move_current_row_start()
    nav.move_prev_col()
    nav.move_current_row_start()