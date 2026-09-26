from collections import deque

class MinStack:

    def __init__(self):
        self._items = deque()
        self._mins = deque()

    def push(self, val: int) -> None:
        self._items.append(val)
        if not self._mins:
            self._mins.append(val)
        else:
            self._mins.append(min(val, self._mins[-1]))

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        self._items.pop()
        self._mins.pop()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def getMin(self) -> int:
        if self.is_empty():
            raise IndexError("getMin from an empty stack")
        return self._mins[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0
