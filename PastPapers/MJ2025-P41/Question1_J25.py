Queue=[-1 for i in range(0,20)]
HeadPointer=-1
TailPointer=-1
NumberItems=0

def Enqueue(Data):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems==20:
        return False
    else:
        if TailPointer<=-1:
            HeadPointer=0
            TailPointer=0
            Queue[TailPointer]=Data
        else:
            TailPointer+=1
            if TailPointer==20:
                TailPointer=0
            Queue[TailPointer]=Data
            NumberItems+=1
        return True

def Dequeue():
    global HeadPointer, TailPointer, NumberItems
    if NumberItems==0:
        return -1
    else:
        Data=Queue[HeadPointer]
        if HeadPointer==19:
            HeadPointer=0
        else:
            HeadPointer+=1
        NumberItems-=1
        return Data


#main program
for x in range(0,25):
    status=Enqueue(x)
    if status==False:
        print("unsuccessful")
    else:
        print("successful")
Removed=Dequeue()
print(Removed)
Removed=Dequeue()
print(Removed)        

