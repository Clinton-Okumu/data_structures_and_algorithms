"""
A **Linked List** is a **linear**, **dynamic** data structure where elements (called **nodes**) are stored in **separate memory locations** and connected by **pointers**.

Each node has:
- A **value**
- A **reference to the next node**

---

## 🧠 Real-Life Examples

- Music playlist (next/previous song)
- Web browser history (next/prev page)
- Implementing stacks and queues

---

## 🧩 Types of Linked Lists

| Type            | Description                      |
|------------------|----------------------------------|
| Singly Linked    | Each node points to next node    |
| Doubly Linked    | Each node points to next and previous node |
| Circular Linked  | Last node points back to head    |

---
"""


# Define Node first
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Now define LinkedList using Node
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        curr = self.head
        if curr and curr.value == value:
            self.head = curr.next
            return
        while curr and curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return
            curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")
