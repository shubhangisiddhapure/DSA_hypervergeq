
def Enqueue():
    if len(q)==size: 
        print("Queue is Full")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")
def dequeue():
    if not q:
        print("Queue is Empty!!!")
    else:
        e=q.pop(0)
        print("element removed!!:",e)
def display():
    while True:
        print("Select the Operation:1.Add 2.Delete 3. Display 4. Quit")
        choice=int(input())
        if choice==1:
            Enqueue()
        elif choice==2:
            dequeue()
        elif choice==3:
            print(q)
        elif choice==4:
            break
        else:
            print("Invalid Option!!!")
q=[1,2,4]
print(q)
size=int(input("Enter the size of Queue:"))
display()