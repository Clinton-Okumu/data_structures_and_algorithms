"""
A **stack** is a **LIFO** (Last In First Out) data structure:
- The last item added is the first one removed.
- Think of a stack of plates or browser history.


## 🔧 Stack Operations

| Operation | Description              | Time Complexity |
|-----------|--------------------------|-----------------|
| `push`    | Add item to the top      | O(1)            |
| `pop`     | Remove and return top item | O(1)          |
| `peek`    | Return top item without removing | O(1)      |
| `is_empty`| Check if stack is empty  | O(1)            |

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
