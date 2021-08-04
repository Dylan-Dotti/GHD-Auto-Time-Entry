
if __name__ == '__main__':
    import app.auto_gui.keyboard_controller as kc
    import app.auto_gui.window_controller as wc
    import time

    wc.set_window_foreground()
    wc.wait_for_window_foreground()
    time.sleep(.5)
    kc.write_text('10000')
    kc.press_key('tab', num_times=2, post_delay=.5)
    kc.write_text('S-003422.01.02.01')
    kc.press_key('enter')
