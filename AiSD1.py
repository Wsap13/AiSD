from typing import Any


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, data: Any) -> None:
        new_node = ListNode(data, self.head)
        self.head = new_node

        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def __str__(self) -> str:
        fake_head: str = ''
        if self.count == 0:
            a = 'Lista jest pusta'
            return a
        else:
            position = self.head
            while position is not None:
                fake_head += str(position.data)
                if position.next:
                    fake_head += '->'
                position = position.next
            return fake_head

    def append(self, data: Any) -> None:
        new_node = ListNode(data)
        if self.count == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def node(self, at: int):
        position = self.head
        noumber = 0
        a = 'Nie mozna podawać wartośći ujemnej'
        b = f'Nie mozna podawać wartośći większej od: {self.count - 1}'
        if at < 0:
            return a
        if at > self.count - 1:
            return b
        while position is not None:
            if noumber == at:
                return position.data
            noumber += 1
            position = position.next

    def insert(self, data: any, after):
        noumber = 1
        position = self.head
        while noumber == after and position is not None:
            position = position.next
            noumber += 1
        temp = ListNode(data)
        temp.next = position.next
        position.next = temp
        self.count += 1

    def __len__(self):
        return self.count

    def pop(self) -> Any:
        if self.head is not None:
            tmp = self.head.data
            self.head = self.head.next
            self.count -= 1
            return tmp

    def remove_last(self) -> Any:

        if self.head is not None:
            if self.count == 0:
                self.pop()
                return
            fake_head: ListNode = self.head
            self.count -= 1
            while fake_head.next.next is not None:
                    fake_head = fake_head.next
            tmp = fake_head.next.data
            self.tail = fake_head.data
            fake_head.next = None
            return tmp

    def remove(self, after):
        position = 0
        headNode = self.head
        if after == 0:
            self.head = self.head.next
            return
        while headNode:
            if position == after - 1:
                headNode.next = headNode.next.next
                break
            headNode = headNode.next
            position += 1
        self.count -= 1


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()
        self.count = 0

    def push(self, data: Any) -> None:
        self._storage.append(data)
        self.count += 1

    def __str__(self) -> str:
        fake_head: str = ''
        position: ListNode = self._storage.head
        if self.count == 0:
            a = 'Stos jest pusty'
            return a
        else:
            while position is not None:
                fake_head += str(position.data)
                if position.next:
                    fake_head += '\n'
                position = position.next
            return fake_head

    def pop(self) -> Any:
        self.count -= 1
        return self._storage.pop()

    def __len__(self):
        return self.count


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()
        self.count = 0

    def __str__(self) -> str:
        position: ListNode = self._storage.head
        fake_head: str = ''
        if self.count == 0:
            a = 'Kolejka jest pusta'
            return a
        else:
            while position:
                fake_head += str(position.data)
                if position.next:
                    fake_head += '|'
                position = position.next
        return fake_head

    def __len__(self):
        return self.count

    def peek(self) -> Any:
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)
        self.count += 1

    def dequeue(self) -> Any:
        self.count -= 1
        return self._storage.pop()


Lista = LinkedList()
Lista.push('tail')
Lista.push('A')
Lista.push(-5.5)
Lista.push(8)
Lista.push(7)
Lista.push(4)
print(Lista)
print(len(Lista))
Lista.remove(4)
print(Lista)
print(len(Lista))
Lista.remove_last()
print(Lista)
print(len(Lista))
print(Lista.node(8))
print(Lista.node(3))
print('Stack')

stack = Stack()
stack.push(3)
stack.push('pies')
print(stack)
print("/")
print(len(stack))
stack.pop()
print('Pop')
print(stack)
print(len(stack))
len(stack)

print('Kułełe')
kueue = Queue()
kueue.enqueue(5)
kueue.enqueue('Kolejka')
kueue.enqueue('Górska')
kueue.enqueue(3)
print(kueue)
print(len(kueue))
print(kueue.peek())
print(len(kueue))
kueue.dequeue()
print(kueue)
print(len(kueue))
"""
Lista.append('stół')
Lista.print()
print()
print(Lista.count)
Lista.insert('Koło', 1)
Lista.print()
print()
print(Lista.count)
"""