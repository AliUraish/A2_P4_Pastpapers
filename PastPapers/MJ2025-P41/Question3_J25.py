class Node:
    def __init__(self, Nodedatap):
        self._Nodedata=Nodedatap
        self._LeftNode=None
        self._RightNode=None
    def GetLeft(self):
        return self._LeftNode
    def GetRight(self):
        return self._RightNode
    def getData(self):
        return self._Nodedata
    def SetLeft(self, Node):
        self._LeftNode=Node
    def SetRight(self, Node):
        self._RightNode=Node


class Tree:
    def __init__(self, firstnode):
        self._FirstNode=firstnode
    def GetRootNode(self):
        return self._FirstNode
    def insert(self, newnode):
        currentnode=self._FirstNode
        inserted=True
        while inserted:
            if newnode.getData()<currentnode.getData():
                if currentnode.GetLeft()==None:
                    currentnode.SetLeft(newnode)
                    return True
                else:
                    currentnode=currentnode.GetLeft()
            else:
                newnode.getData()>currentnode.getData()
                if currentnode.GetRight()==None:
                    currentnode.SetRight(newnode)
                    return True
                else:
                    currentnode=currentnode.GetRight()


def OutputInOrder(Node):
    if Node.GetLeft()!=None:
        OutputInOrder(Node.GetLeft())
    print (Node.getData())
    if Node.GetRight()!=None:
        OutputInOrder(Node.GetRight())


#main program
Node1=Node(10)
Node2=Node(20)
Node3=Node(5)
Node4=Node(15)
Node5=Node(7)
ObjectTree=Tree(Node1)
ObjectTree.insert(Node2)
ObjectTree.insert(Node3)
ObjectTree.insert(Node4)
ObjectTree.insert(Node5)
OutputInOrder(ObjectTree.GetRootNode())