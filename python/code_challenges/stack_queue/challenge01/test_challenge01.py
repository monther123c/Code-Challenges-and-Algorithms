# Write your test here
import pytest
from challenge01 import myQueue

def test_push():
    q = myQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    expected = 1
    actual = q.peek()
    assert actual == expected

def test_pop():
    q = myQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    expected = 1
    actual = q.pop()
    assert actual == expected


def test_empty():
    q = myQueue()

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    expected = False
    actual = q.empty()
    assert actual == expected

def test_empty1():
    q = myQueue()

    q.push(1)
    q.push(2)
    q.pop()
    q.pop()
    expected = True
    actual = q.empty()
    assert actual == expected
