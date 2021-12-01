# Queue

maxval=int(input("Enter Maximum size of stack:"))
top = 0
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Push(self, item):
        self.items.insert(0,item)

    def Pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def Display(self):
        return self.items

myq = Queue()
cnd = True
while cnd:
 print("1.Push")
 print("2.Pop")
 print("3.Display")
 print("4.Quit")
 ch=int(input("Enter your choice:"))
 if ch==1:
   if top<maxval:
     elem=int(input("Enter any integer element:"))
     myq.Push(elem)
     top+=1
     print("Element", elem, "pushed into the Queue")
   else:
    print("Queue Overflow")
 elif ch==2:
   myq.Pop()
   top-=1
   print("Element popped from the Queue")
 elif ch==3:
   print(myq.Display())
 else:
  print("Exit")
  cnd = False
