from sortedcontainers import SortedList


class MaxStack:

    def __init__(self):
        self.stk = SortedList()      # (index, value)
        self.values = SortedList()   # (value, index)
        self.cnt = 0

    def push(self, x: int) -> None:
        self.stk.add((self.cnt, x))
        self.values.add((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        idx, val = self.stk.pop()

        # Remove the same element from the value-sorted list.
        self.values.remove((val, idx))

        return val

    def top(self) -> int:
        return self.stk[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, idx = self.values.pop()

        # Remove the same element from the stack-sorted list.
        self.stk.remove((idx, val))

        return val