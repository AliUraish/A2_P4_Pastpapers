

StackData=[0,0,0,0,0,0,0,0,0,0]
StackPointer=0

def Outputelements():
    global StackData
    global StackPointer
    print(StackPointer)
    for x in range(0,10):
        print(StackData[x])


def push(number):
    global StackData
    global StackPointer
    if StackPointer==10:
        return False
    else:
        StackData[StackPointer]=number
        StackPointer=StackPointer+1
        return True




def pop():
    if StackPointer==0:
        return -1
    else:
        Return=StackData[StackPointer-1]
        StackPointer=StackPointer-1
        return Return


#main
for x in range(0,11):
    Number=int(input("Enter a number"))
    if push(Number)==True:
        print("stored")
    else:
        print("Stack is full")

Outputelements()
pop()
pop()
Outputelements()