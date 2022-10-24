# Write here the code challenge solution
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

    def find_middle(self):
        """This function will return the mid value of the linked list"""
        counter=0
        current=self.head
        while current is not None:
            prev=current
            current = current.next
            counter+=1
        if counter==1:
            print("the mid is ",prev.value)
            return prev.value
        elif counter==0:
            print ("the list is empty")
            return "the list is empty"        
        elif counter % 2 ==1:    
           mid=counter/2 + 0.5
        elif counter % 2 ==0:
            mid=counter/2+1   
        
        counter=1
        current=self.head
        while current.next is not None:
            current = current.next
            counter+=1
            if counter==mid:
                print("the mid is ",current.value)
                return current.value   


    def printAll(self):
        """this is for printing"""
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
     
    def OutTest(self):
        """this is for testing"""
        lst=[]
        if self.head is None:
            return"The linked list is empty"
        else:
            current = self.head
            while current is not None:
                lst.append(current.value)
                current = current.next
        return lst            


#####
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

linkedList1.printAll()        

linkedList1.find_middle()                                     
