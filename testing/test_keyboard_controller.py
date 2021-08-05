
if __name__ == '__main__':
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_main_window_controller import SapMainWindowController
    import time

    wc = SapMainWindowController()
    wc.set_window_foreground()
    wc.wait_for_window_foreground()
    time.sleep(.5)
    kc = KeyboardController(wc)
    kc.write_text('10000')
    kc.press_key('tab', num_times=2, post_delay=.5)
    kc.write_text('S-003422.01.02.01')
    kc.press_key('enter')
