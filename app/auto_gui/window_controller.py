from typing import List
import win32gui as wgui
import win32con as wcon
import time

class WindowController:

    def __init__(self, window_name: str, alternate_names=[], find_window_timeout=None) -> None:
        self._window = self._find_window([window_name] + alternate_names, find_window_timeout)

    def is_window_foreground(self):
        return wgui.GetForegroundWindow() == self._window

    def wait_for_window_foreground(self, check_interval=.5):
        while not self.is_window_foreground():
            time.sleep(check_interval)

    def set_window_foreground(self):
        if self.is_window_minimized():
            wgui.ShowWindow(self._window, wcon.SW_RESTORE)
            time.sleep(.5)
        else:
            wgui.SetForegroundWindow(self._window)
            time.sleep(.05)

    def is_window_minimized(self):
        return wgui.IsIconic(self._window) == 1
    
    def _find_window(self, window_names: List[str], find_window_timeout=None, check_interval=.5):
        window_names_str = '/'.join(window_names)
        start_time = time.time()
        print('Finding window: %s...' % '/'.join(window_names))
        while True:
            for window_name in window_names:
                window = wgui.FindWindow(None, window_name)
                if window != 0:
                    return window
            if find_window_timeout is not None and (time.time() - start_time) >= find_window_timeout:
                raise TimeoutError('Timed out attempting to find window: ' + window_names_str)
            time.sleep(check_interval)
