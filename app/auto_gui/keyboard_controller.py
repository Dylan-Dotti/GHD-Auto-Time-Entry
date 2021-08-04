import app.auto_gui.window_controller as wc
import pyautogui as pag
import time


def press_key(key_name, num_times=1, duration=0, interval=0):
    for _ in range(num_times):
        press_key_down(key_name)
        if duration > 0 and wc.is_window_foreground():
            time.sleep(duration)
        press_key_up(key_name)
        if interval > 0 and wc.is_window_foreground():
            time.sleep(interval)


def press_key_sequence(*keys):
    _wait_for_window_foreground()
    pag.hotkey(*keys)


def press_key_down(key_name):
    _wait_for_window_foreground()
    pag.keyDown(key_name)


def press_key_up(key_name):
    _wait_for_window_foreground()
    return pag.keyUp(key_name)


def press_tab():
    press_key('tab')


def press_enter():
    press_key('enter')


def press_esc():
    press_key('esc')


def press_f2():
    press_key_sequence('fn', 'f2')


def alt_tab():
    press_key_sequence('alt', 'tab')


def write_text(text):
    _wait_for_window_foreground()
    pag.write(text)


def _wait_for_window_foreground():
    if not wc.is_window_foreground():
        print('waiting for window to be foreground for key event...')
        wc.wait_for_window_foreground()
