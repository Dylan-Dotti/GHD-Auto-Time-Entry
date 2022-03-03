from typing import List
from app.interfaces.stoppable import Stoppable
from app.interfaces.threadsafe_stoppable import ThreadSafeStoppable


class ThreadSafeStoppableWithSubComponents(ThreadSafeStoppable):

    def __init__(self) -> None:
        super().__init__()
        self._subcomponents: List[Stoppable] = []
    
    def stop(self):
        self._stop_lock.acquire()
        super().stop()
        self.stop_subcomponents()
        self._stop_lock.release()
    
    def add_stoppable_subcomponent(self, sub_comp: Stoppable) -> bool:
        self._stop_lock.acquire()
        if sub_comp not in self._subcomponents:
            self._subcomponents.append(sub_comp)
            self._stop_lock.release()
            return True
        self._stop_lock.release()
        return False
    
    def remove_stoppable_subcomponent(self, sub_comp: Stoppable) -> bool:
        self._stop_lock.acquire()
        if sub_comp in self._subcomponents:
            self._subcomponents.remove(sub_comp)
            self._stop_lock.release()
            return True
        self._stop_lock.release()
        return False
    
    def clear_subcomponents(self):
        self._subcomponents.clear()
    
    def stop_subcomponents(self) -> None:
        self._stop_lock.acquire()
        for comp in self._subcomponents:
            comp.stop()
        self._stop_lock.release()