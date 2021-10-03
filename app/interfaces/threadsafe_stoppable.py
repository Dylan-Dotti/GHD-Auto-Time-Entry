from app.interfaces.stoppable import Stoppable
from app.interfaces.stop_requested_error import StopRequestedError
from threading import RLock

class ThreadSafeStoppable(Stoppable):

    def __init__(self) -> None:
        super().__init__()
        self._stop_requested = False
        self._stop_lock: RLock = RLock()

    def stop(self):
        self._stop_requested = True

    def _on_stop_request_acknowledge(self):
        self._stop_requested = False
        raise StopRequestedError()