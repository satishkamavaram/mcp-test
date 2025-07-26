"""
stack.py

A simple Stack implementation in Python with push and pop operations.

Usage:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    value = stack.pop()  # value == 2
"""

class Stack:
    """A simple stack implementation using a Python list."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self):
        """Pop the top item off the stack and return it.
        Raises IndexError if the stack is empty.
        """
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def __repr__(self):
        return f"Stack({self._items})"
