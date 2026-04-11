QueueArray=["" for i in range(0, 10)]
headpointer=0
tailpointer=0
NumberItems=0

def Enqueue(DataToAdd):
    global headpointer, tailpointer, NumberItems
    if NumberItems==10:
        return False
    QueueArray[tailpointer]=DataToAdd
    if tailpointer>=9:
        tailpointer==0
    else:
        tailpointer=tailpointer+1
    NumberItems=NumberItems+1
    return True


def Dequeue():
    global headpointer, tailpointer, NumberItems
    if NumberItems==0:
        return False
    remove=QueueArray[tailpointer]
    if tailpointer==0:
        tailpointer=9
    else:
        tailpointer=tailpointer-1
    NumberItems=NumberItems-1
    return remove


#main program
for x in range(0,10):
    datatoadd=input("enter the value")
    Status=Enqueue(datatoadd)
    if Status==False:
        print("Queue is full not able to add")
    else:
        print("Value added")

offload=Dequeue()
print(offload)
offload=Dequeue()
print(offload)






    
