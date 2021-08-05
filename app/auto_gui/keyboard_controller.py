from app.auto_gui.window_controller import WindowController
import pyautogui as pag
import time

class KeyboardController:

    def __init__(self, window_controller: WindowController) -> None:
        self._wc = window_controller

    def press_key(self, key_name, num_times=1, duration=0, post_delay=0):
        for _ in range(num_times):
            self.press_key_down(key_name)
            if duration > 0 and self._wc.is_window_foreground():
                time.sleep(duration)
            self.press_key_up(key_name)
            if post_delay > 0 and self._wc.is_window_foreground():
                time.sleep(post_delay)

    # kwargs:
    #   num_times - number of times to press the sequence. Default 1
    #   post_delay - num seconds to wait after sequence. Default 0
    def press_key_sequence(self, *keys, **kwargs) -> None:
        num_times = kwargs.pop('num_times', 1)
        post_delay = kwargs.pop('post_delay', 0)
        for _ in range(num_times):
            self._wait_for_window_foreground()
            pag.hotkey(*keys)
            if post_delay > 0:
                time.sleep(post_delay)

    def press_key_down(self, key_name) -> None:
        self._wait_for_window_foreground()
        pag.keyDown(key_name)

    def press_key_up(self, key_name) -> None:
        self._wait_for_window_foreground()
        return pag.keyUp(key_name)

    def press_f2(self, num_times=1, post_delay=0) -> None:
        self.press_key_sequence('fn', 'f2', num_times=num_times, post_delay=post_delay)

    def press_enter(self, num_times=1, post_delay=0) -> None:
        self.press_key('enter', num_times=num_times, post_delay=post_delay)

    def press_esc(self, num_times=1, post_delay=0) -> None:
        self.press_key('esc', num_times=num_times, post_delay=post_delay)

    def press_tab(self, num_times=1, post_delay=0) -> None:
        self.press_key('tab', num_times=num_times, post_delay=post_delay)

    def press_reverse_tab(self, num_times=1, post_delay=0) -> None:
        self.press_key_sequence('shift', 'tab', num_times=num_times, post_delay=post_delay)

    def write_text(self, text, post_delay=0) -> None:
        self._wait_for_window_foreground()
        pag.write(text)
        if post_delay > 0:
            time.sleep(post_delay)

    def _wait_for_window_foreground(self) -> None:
        if not self._wc.is_window_foreground():
            print('waiting for window to be foreground for key event...')
            self._wc.wait_for_window_foreground()
