# Using Linked Lists lol

class Queue:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.stack = Queue(-1) # dummy
        self.head = self.tail = self.stack

    def push(self, x: int) -> None:
        node = Queue(x)
        node.next = self.stack.next if self.stack else None
        self.stack.next = node

    def pop(self) -> int:
        pop = self.stack.next if self.stack else None
        self.stack.next = pop.next if pop else None
        pop.next = None if pop else None
        return pop.val

    def top(self) -> int:
        return self.stack.next.val if self.stack.next else None

    def empty(self) -> bool:
        return True if self.stack and not self.stack.next else False  # this line was tricky


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()