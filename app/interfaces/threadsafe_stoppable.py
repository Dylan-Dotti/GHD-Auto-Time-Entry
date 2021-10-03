from app.interfaces.stoppable import Stoppable
from threading import RLock

class ThreadSafeStoppable(Stoppable):

    def __init__(self) -> None:
        super().__init__()
        self._stop_lock: RLock = RLock()