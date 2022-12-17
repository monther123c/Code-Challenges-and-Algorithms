# Write your test here
import pytest

from challenge01 import Node,Edge,Graph

def test_zero():
    graph1 = Graph()

    a = graph1.add_node("I")
    b = graph1.add_node("H")
    c = graph1.add_node("A")
    d = graph1.add_node("B")
    
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    actual = len(graph1.BreadthFirst(a))
    excepted= 4
    assert excepted == actual
    
def test_one():
    graph1 = Graph()

    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    actual = graph1.BreadthFirst(a)
    excepted= ['A','B','C','D']
    assert excepted == actual
    
    
def test_tow():
    graph1 = Graph()

    a = graph1.add_node(1)
    b = graph1.add_node(2)
    c = graph1.add_node(3)
    d = graph1.add_node(4)
    
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    actual = graph1.BreadthFirst(d)
    excepted= [4,2,3,1]
    assert excepted == actual