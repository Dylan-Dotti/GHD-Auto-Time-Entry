
if __name__ == '__main__':
    import app.auto_gui.window_controller as wc
    from app.auto_gui.sap_window_navigator import SapWindowNavigator
    import time

    wc.set_window_foreground()
    wc.wait_for_window_foreground()

    nav = SapWindowNavigator()
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