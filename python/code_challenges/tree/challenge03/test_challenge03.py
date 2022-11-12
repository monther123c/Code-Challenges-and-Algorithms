# Write your test here
from challenge03 import Node,Tree

tree=Tree()

def test_balanced_tree_1():

    root=tree.convert_to_bts([1,2,3])
    tree.tree_list=[root.value]
    actual=tree.display_tree(root)
    expect=[2,1,3,'null','null','null','null',]
    assert actual == expect


def test_balanced_tree_2():

    root=tree.convert_to_bts([])
    try:
        tree.tree_list=[root.value]
    except AttributeError:
        tree.tree_list=[root]
    finally:
    
        actual=tree.display_tree(root)
        expect=['null']
    assert actual == expect


def test_balanced_tree_3():

    root=tree.convert_to_bts([-10,-3,0,5,9])
    try:
        tree.tree_list=[root.value]
    except AttributeError:
        tree.tree_list=[root]
    finally:
    
        actual=tree.display_tree(root)
        expect=[0,-3,9,-10,'null','null','null',5,'null','null','null']
    assert actual == expect
