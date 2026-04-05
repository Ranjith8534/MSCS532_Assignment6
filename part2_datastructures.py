# -----------------------------
# ARRAY (Python List)
# -----------------------------
class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, value):
        self.data.remove(value)

    def access(self, index):
        return self.data[index]


# -----------------------------
# STACK
# -----------------------------
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


# -----------------------------
# QUEUE
# -----------------------------
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)


# -----------------------------
# LINKED LIST
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        values = []
        while temp:
            values.append(temp.data)
            temp = temp.next
        return values


# -----------------------------
# TEST BLOCK
# -----------------------------
if __name__ == "__main__":
    # ARRAY
    arr = Array()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    arr.delete(20)
    print("Array:", arr.data, "Access index 1:", arr.access(1))

    # STACK
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack pop:", stack.pop(), "Peek:", stack.peek())

    # QUEUE
    queue = Queue()
    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)
    print("Queue dequeue:", queue.dequeue(), "Queue now:", queue.queue)

    # LINKED LIST
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.delete(10)
    print("Linked List:", ll.traverse())