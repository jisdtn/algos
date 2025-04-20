# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from __future__ import annotations


class NestedInteger:

    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value

    def isInteger(self) -> bool:
       return self._integer is not None

    def getInteger(self) -> int:
       return self._integer

    def getList(self) -> list[NestedInteger]:
       return self._list

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False


def build_nested(data):
    if isinstance(data, int):
        return NestedInteger(data)
    return NestedInteger([build_nested(x) for x in data])


if __name__ == '__main__':
    nested = build_nested([[1,1],2,[1,1]])
    i, v = NestedIterator(nested.getList()), []
    while i.hasNext():
        v.append(i.next())
    print(v)


