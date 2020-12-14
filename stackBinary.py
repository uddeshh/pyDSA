# n=int(input())
# re=''
# while n>=1:
#     if n==1:
#         re='1'+re
#         break
#     if n%2==0:
#         re='0'+re
#         n=int(n/2)
#     else:
#         if n!=1:
#             re='1'+re
#             n=int((n-1)/2)
# print(re)

class Stack:

    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.insert(0,item)
    def pull(self):
        self.items.pop()
    def last(self):
        return self.items[-1]
    def print_it(self):
        return self.items

s=Stack()
n=int(input())
while n>=0:
    if n==1:
        s.push(1)
        break
    if n==0:
        s.push(0)
        break
    if n%2==0:
        s.push(0)
        n=n/2
    else:
        s.push(1)
        n=(n-1)/2
print(*(s.print_it()),sep='')
