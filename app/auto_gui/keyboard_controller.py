import app.auto_gui.window_controller as wc
import pyautogui as pag
import time


def press_key(key_name, num_times=1, duration=0, post_delay=0):
    for _ in range(num_times):
        press_key_down(key_name)
        if duration > 0 and wc.is_window_foreground():
            time.sleep(duration)
        press_key_up(key_name)
        if post_delay > 0 and wc.is_window_foreground():
            time.sleep(post_delay)


# kwargs:
#   num_times - number of times to press the sequence. Default 1
#   post_delay - num seconds to wait after sequence. Default 0
def press_key_sequence(*keys, **kwargs):
    num_times = kwargs.pop('num_times', 1)
    post_delay = kwargs.pop('post_delay', 0)
    for _ in range(num_times):
        _wait_for_window_foreground()
        pag.hotkey(*keys)
        if post_delay > 0:
            time.sleep(post_delay)


def press_key_down(key_name):
    _wait_for_window_foreground()
    pag.keyDown(key_name)


def press_key_up(key_name):
    _wait_for_window_foreground()
    return pag.keyUp(key_name)


def press_f2(num_times=1, post_delay=0):
    press_key_sequence('fn', 'f2', num_times=num_times, post_delay=post_delay)


def press_enter(num_times=1, post_delay=0):
    press_key('enter', num_times=num_times, post_delay=post_delay)


def press_esc(num_times=1, post_delay=0):
    press_key('esc', num_times=num_times, post_delay=post_delay)


def press_tab(num_times=1, post_delay=0):
    press_key('tab', num_times=num_times, post_delay=post_delay)


def press_reverse_tab(num_times=1, post_delay=0):
    press_key_sequence('shift', 'tab', num_times=num_times, post_delay=post_delay)


def write_text(text, post_delay=0):
    _wait_for_window_foreground()
    pag.write(text)
    if post_delay > 0:
        time.sleep(post_delay)


def _wait_for_window_foreground():
    if not wc.is_window_foreground():
        print('waiting for window to be foreground for key event...')
        wc.wait_for_window_foreground()
