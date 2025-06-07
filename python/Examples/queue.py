"""
A **queue** is a **FIFO** (First In, First Out) data structure:
- The first element added is the first one removed.
- Think of people standing in line or print jobs.

---



## 🔧 Queue Operations

| Operation | Description               | Time Complexity |
|-----------|---------------------------|-----------------|
| `enqueue` | Add item to rear/tail     | O(1)            |
| `dequeue` | Remove item from front/head | O(1)         |
| `peek`    | Return front without removing | O(1)        |
| `is_empty`| Check if queue is empty   | O(1)            |

"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)
