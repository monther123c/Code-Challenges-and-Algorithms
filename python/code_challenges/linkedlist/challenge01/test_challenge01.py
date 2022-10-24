import pytest
from challenge01 import Node,LinkedList,pop_at
 # test the code                 
MyList = LinkedList()

#Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#delete

def test_delete():
    pop_at(1)
    expected=["10","30" ,"40","10", "20", "30"]
    actual=MyList.transfer_to_list()
    assert expected==actual


