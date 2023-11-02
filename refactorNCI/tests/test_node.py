
import sys
sys.path.append("./refactorNCI")

from main import *

dL = DoublyLinkedList()



for i in range(4):
    dL.add_last(Node(i))

def test_add():
    """Test add"""
    node = Node(1)
    assert node.get_element() == 1

def testDoublelyLinked():

    assert str(dL) == f"(0, (1, (2, (3, ('Trailer', None)))))"

def testSize():
    assert dL.size() == 4  

def testIsEmpty():
    dL2 = DoublyLinkedList()
    assert dL.is_empty() == False
    assert dL2.is_empty() == True
    del dL2

def testFirstandLast():
    assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"
    assert str(dL.get_last()) == f"(3, ('Trailer', None))"

def testgetprefandlast():
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"

def testaddbf():
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())
    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"

def testaddfirst():
    dL.add_first(Node(7))
    dL.add_last(Node(-1))
    assert str(dL) == "(7, (0, (42, (1, (2, (34, (3, (-1, ('Trailer', None)))))))))"

def testremove():
    dL.remove(dL.get_first())
    assert dL.get_first().get_element() == 0

def testlambda():
    dL.map(lambda x: x**2)
    assert str(dL) == "(0, (1764, (1, (4, (1156, (9, (1, ('Trailer', None))))))))"