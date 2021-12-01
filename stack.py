# Stack

maxval=int(input("Enter Maximum size of stack:"))
top = 0
def createStack():
 stack=[]
 return stack
def isEmpty(stack):
 return len(stack)==0
def Push(stack,item):
 stack.append(item)
 print("Pushed to Stack",item)
def Pop(stack):
 if isEmpty(stack):
  return "Stack Underflow"
 return stack.pop()
stack=createStack()
cnd = True
while cnd:
 print("1.Push")
 print("2.Pop")
 print("3.Display")
 print("4.Quit")
 ch=int(input("Enter your choice:"))
 if ch==1:
   if top<maxval:
     item=int(input("Enter any integer element:"))
     Push(stack,item)
     top+=1
   else:
    print("Stack Overflow")
 elif ch==2:
   print(Pop(stack))
   top-=1
 elif ch==3:
   print(stack)
 else:
  print("Exit")
  cnd = False
