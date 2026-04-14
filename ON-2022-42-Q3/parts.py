Queue=[]
head=-1
tail=0

def Enqueue(Record):
    global tail, Queue, head
    if tail==100:
        return False
    else:
        Queue[tail]=Record
        tail+=1
        if head==-1:
            head=0
        return True
    
store=False
for Count in range(100):
    store=Enqueue(Count)
    if store==False:
        print("Unsuccessful")
    else:
        print("Successful")

def RecursiveOutput(Start):
    global Queue, tail, head
    if Start==0:
        return Queue[Start]
    else:
        return Queue[Start]+RecursiveOutput(Start-1)

    #main program
    print(str(RecursiveOutput(tail-1)))

    