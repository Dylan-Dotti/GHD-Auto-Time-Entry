from app.interfaces.stoppable import Stoppable
from typing import List
import win32gui as wgui
import win32con as wcon
import time

class WindowController(Stoppable):

    def __init__(self) -> None:
        self._is_finding_window = False
        self._stop_requested = False
        self._window = None

    #def __init__(self, window_name: str, alternate_names=[], find_window_timeout=None) -> None:
    #    self.__init__()
    #    self._window = self.bind_to_window([window_name] + alternate_names, find_window_timeout)
    
    def bind_to_window(self, window_names: List[str], find_window_timeout = None):
        self._window = self._find_window(window_names, find_window_timeout)
        print('bind_to_window end')
        self._stop_requested = False
    
    def stop(self):
        print('Stopping window_controller')
        self._stop_requested = self._is_finding_window

    def is_window_foreground(self):
        return self._window is None or wgui.GetForegroundWindow() == self._window

    def wait_for_window_foreground(self, check_interval=.1):
        while not self.is_window_foreground() and not self._stop_requested:
            time.sleep(check_interval)
        self._stop_requested = False

    def set_window_foreground(self):
        if self._window is None:
            return
        if self.is_window_minimized():
            wgui.ShowWindow(self._window, wcon.SW_RESTORE)
            time.sleep(.5)
        else:
            wgui.SetForegroundWindow(self._window)
            time.sleep(.05)

    def is_window_minimized(self):
        return wgui.IsIconic(self._window) == 1
    
    def _find_window(self, window_names: List[str], find_window_timeout=None, check_interval=.5):
        self._is_finding_window = True
        window_names_str = '/'.join(window_names)
        start_time = time.time()
        print('Finding window: %s...' % '/'.join(window_names))
        while not self._stop_requested:
            for window_name in window_names:
                window = wgui.FindWindow(None, window_name)
                if window != 0:
                    self._is_finding_window = False
                    return window
            if self._stop_requested:
                break
            if find_window_timeout is not None and (time.time() - start_time) >= find_window_timeout:
                raise TimeoutError('Timed out attempting to find window: ' + window_names_str)
            time.sleep(check_interval)
        self._is_finding_window = False
        return None
