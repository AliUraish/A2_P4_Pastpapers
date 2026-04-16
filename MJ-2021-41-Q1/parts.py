class node:
    def __init__(self, thedata, nextNodeNumber):
        self.data = thedata
        self.nextNode = nextNodeNumber


startPointer=0
emptyList=5

linkedList=[node(1,1), node(5,4), node(6,7), node(7,-1), node(2, 2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]

def outputNodes(LinkedList, startPointer):
    currentpointer=startPointer
    while currentpointer!=-1:
        print(LinkedList[currentpointer].data)
        currentpointer=LinkedList[currentpointer].nextNode



def AddNode(LinkedList, emptyList, startpointer):
    datainput = int(input("Enter data: "))
    if emptyList < 0 or emptyList > 9:
        return False, emptyList, startpointer
    else:
        nextFree = LinkedList[emptyList].nextNode  
        LinkedList[emptyList].data = datainput
        LinkedList[emptyList].nextNode = -1        
        
        if startpointer == -1:                     
            startpointer = emptyList               
        else:
            currentPointer = startpointer
            while LinkedList[currentPointer].nextNode != -1:  
                currentPointer = LinkedList[currentPointer].nextNode
            LinkedList[currentPointer].nextNode = emptyList   
        
        emptyList = nextFree
        return True, emptyList, startpointer

#main program
outputNodes(linkedList, startPointer)
result=AddNode(linkedList, emptyList, startPointer)
if result[0]==False:
    print("Unsuccessful")
else:
    print("Successful")
outputNodes(linkedList, startPointer)


