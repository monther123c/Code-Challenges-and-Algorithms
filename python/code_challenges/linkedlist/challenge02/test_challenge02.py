# Write your test here
from platform import node
import pytest 
from challenge02 import Node , linkedlist

def test_append():
    run=odd_fun()
    actual=run.test_fun()
    expected=["A","B","C","D","E"]
    assert actual==expected


def test_one_element():
    
    one=linkedlist()
    node_one=Node("A")
    one.append(node_one)
    actual=one.find_middle()
    expected="A"
    assert actual==expected


def test_odd():
    run=odd_fun()
    
    actual=run.find_middle()
    expected="C"
    assert actual==expected

def test_even():
    run=even_fun()
    actual=run.find_middle()
    expected="C"
    assert actual==expected
    
def test_empty():
    empty=linkedlist()

    actual= empty.find_middle()

    expected="the list is empty"
    assert actual==expected

def odd_fun():
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

    return linkedList1

def even_fun():
    linkedList1 = linkedlist()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    return linkedList1        