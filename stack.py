class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def is_empty(self):
        return self.items==[]
    def get_it(self):
        return self.items
    def last(self):
        return self.items[-1]
s=Stack()
x=input()
for i in x:
    if i in '}])':
        if i ==')' and s.last()=='(':
            s.pop()
        elif i =='}' and s.last()=='{':
            s.pop()
        elif i ==']' and s.last()=='[':
            s.pop()
        else:
            break
    else:
        s.push(i)

if len(s.items)!=0:
    print('No')
else:
    print('Yes')
