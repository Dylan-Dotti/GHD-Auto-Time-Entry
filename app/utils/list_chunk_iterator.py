from typing import Generic, List, TypeVar


T = TypeVar('T')

class ListChunkIterator(Generic[T]):

    def __init__(self, list: List[T]) -> None:
        self._list = list.copy()
        self._current_index = 0
    
    def has_next_chunk(self) -> bool:
        return self._current_index < len(self._list)
    
    def get_next_chunk(self, chunk_size: int,
                       pad_end: bool = False,
                       pad_val: T = None) -> List[T]:
        if not self.has_next_chunk():
            return None
        end_index = self._current_index + chunk_size
        chunk = self._list[self._current_index : end_index]
        if pad_end:
            padding = [pad_val for _ in range(chunk_size - len(chunk))]
            chunk.extend(padding)
        self._current_index = end_index
        return chunk