# Write your test here
import pytest
from challenge03 import LinkedList

########### Test 01 ###########
link1= LinkedList()
link1.append_by_tail(1)
link1.append_by_tail(2)
link1.append_by_tail(3)
link1.append_by_tail(4)
link1.append_by_tail(5)

link1.removeNthFromEnd(2)
result= link1.print_list_of_values()

def test_get_middle_node_one():
    '''
        input -> object
        return -> boolean
        '''
        #3 -> 4 -> 5
    expected=[1,2,3,5]
    actual= result
    assert actual==expected

########## Test 02 ###########
link2= LinkedList()
link2.append_by_tail(1)

link2.removeNthFromEnd(1)
result2= link2.print_list_of_values()


def test_get_middle_node_two():
    '''
        input -> object
        return -> boolean
        '''
    expected=[]
    actual= result2
    assert actual==expected

########## Test 03 ###########
link3= LinkedList()
link3.append_by_tail(1)
link3.append_by_tail(2)


link3.removeNthFromEnd(1)
result3= link3.print_list_of_values()

def test_get_middle_node_three():
    '''
        input -> object
        return -> boolean
        '''
    expected=[1]
    actual= result3
    assert actual==expected