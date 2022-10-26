class Node:
    """This class creates the node """
    def __init__(self,value):
        self.value=value
        self.next= None

class linkedlist:
    """this class append and delete a node"""
    def __init__(self):
        self.head=None

    def append(self,node):
        """this is responseble to append a node"""
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = node         
    
    def printAll(self):
        """this is for printing"""
        
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    
    def test_fun(self):
        """this is just for testing"""
        lst=[]

        current = self.head
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst

def delete(node):
    """this is responseble to delete a node"""

    node.value=node.next.value
    node.next=node.next.next




linkedList1 = linkedlist()
node1 = Node("A")
linkedList1.append(node1)

node2 = Node("B")
linkedList1.append(node2)

node3 = Node("C")
linkedList1.append(node3)

node4 = Node("D")
linkedList1.append(node4)

node5 = Node("E")
linkedList1.append(node5)

delete(node3)

linkedList1.printAll() 
             



if __name__=="__main__":
    pass