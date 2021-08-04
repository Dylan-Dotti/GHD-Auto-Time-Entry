import win32gui as wgui
import win32con as wcon
import time


def is_window_foreground():
    return wgui.GetForegroundWindow() == _get_window()


def wait_for_window_foreground(check_interval=1):
    while not is_window_foreground():
        time.sleep(check_interval)


def set_window_foreground():
    if is_window_minimized():
        wgui.ShowWindow(_get_window(), wcon.SW_RESTORE)
        time.sleep(.5)
    else:
        wgui.SetForegroundWindow(_get_window())
        time.sleep(.005)


def is_window_minimized():
    return wgui.IsIconic(_get_window()) == 1


def _get_window():
    global __window
    if __window is None:
        __window = _find_window()
    return __window


def _find_window():
    win_name = 'Time Sheet: Data Entry View'
    window = wgui.FindWindow(None, win_name)
    if window != 0:
        return window
    raise RuntimeError('Could not find VBA window')


__window = None
