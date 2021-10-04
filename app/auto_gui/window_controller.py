from app.interfaces.threadsafe_stoppable import ThreadSafeStoppable
from typing import List
import win32gui as wgui
import win32con as wcon
import time

class WindowController(ThreadSafeStoppable):

    def __init__(self) -> None:
        super().__init__()
        self._window = None
    
    def bind_to_window(self, window_names: List[str], find_window_timeout = None):
        self._stop_requested = False
        self._window = self._find_window(window_names, find_window_timeout)
    
    def stop(self):
        print('Stopping window_controller...')
        super().stop()
    
    def _on_stop_request_acknowledge(self):
        print('WindowController Acknowledging stop request')
        return super()._on_stop_request_acknowledge()

    def is_window_foreground(self):
        return self._window is None or wgui.GetForegroundWindow() == self._window

    def wait_for_window_foreground(self, check_interval=.1):
        self._stop_requested = False
        while not self.is_window_foreground():
            time.sleep(check_interval)
            if self._stop_requested:
                self._on_stop_request_acknowledge()

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
        window_names_str = '/'.join(window_names)
        start_time = time.time()
        print('Finding window: %s...' % '/'.join(window_names))
        while True:
            if self._stop_requested:
                self._on_stop_request_acknowledge()
            for window_name in window_names:
                window = wgui.FindWindow(None, window_name)
                if window != 0:
                    return window
            if find_window_timeout is not None and (time.time() - start_time) >= find_window_timeout:
                raise TimeoutError('Timed out attempting to find window: ' + window_names_str)
            time.sleep(check_interval)
