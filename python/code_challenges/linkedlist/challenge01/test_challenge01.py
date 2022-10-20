import pytest
from challenge01 import Node,LinkedList
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

MyList.pop_at(2)
MyList.PrintList()

MyList.pop_at(1)
MyList.PrintList() 

