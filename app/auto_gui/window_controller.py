import win32gui as wgui
import win32con as wcon
import time

class WindowController:

    def __init__(self, window_name: str) -> None:
        self._window = wgui.FindWindow(None, window_name)
        if self._window == 0:
            raise RuntimeError(
                'Could not find window: ' + window_name)

    def is_window_foreground(self):
        return wgui.GetForegroundWindow() == self._window

    def wait_for_window_foreground(self, check_interval=1):
        while not self.is_window_foreground():
            time.sleep(check_interval)

    def set_window_foreground(self):
        if self.is_window_minimized():
            wgui.ShowWindow(self._window, wcon.SW_RESTORE)
            time.sleep(.5)
        else:
            wgui.SetForegroundWindow(self._window)
            time.sleep(.005)

    def is_window_minimized(self):
        return wgui.IsIconic(self._window) == 1
