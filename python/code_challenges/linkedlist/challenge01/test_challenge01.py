import pytest 
from challenge01 import Node , linkedlist, delete

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


def test_append():
    
    actual=linkedList1.test_fun()
    expected=["A","B","C","D","E"]
    assert actual==expected

def test_delete1():
    
    delete(node1)

    actual=linkedList1.test_fun()
    expected=["B","C","D","E"]
    assert actual==expected

def test_delete2():
    
    delete(node3)

    actual=linkedList1.test_fun()
    expected=["B","D","E"]
    assert actual==expected


