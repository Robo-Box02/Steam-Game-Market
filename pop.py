class Stack:
    def __init__(self,max):
        self.list_el = []
        self.max = max
        ...

    def top(self):
        ...
    def push(self,item):
        if self.size()>=self.max:
            raise ValueError('Stack is Full')
        else:
             return self.list_el.append(item)

    def pop(self,item):
        if self.empty():
            raise ValueError('Stack is Full')
        else:
            self.list_el.append(item)

    def size(self):
        return len(self.list_el)

    def empty(self):
        return len(self.list_el) == 0

stack = Stack(5)
stack.push(1)
stack.push(6)
stack.push(9)
print(stack.top())
