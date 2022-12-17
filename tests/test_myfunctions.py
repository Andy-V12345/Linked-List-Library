from LinkedListFunctionsLib import myfunctions

numList = [1, 2, 3, 4, 5, 6]
ll = myfunctions.createLL(numList)

def test_createLL():
    assert ll.head.data == 1

def test_count():
    assert ll.count() == 6

def test_access():
    assert ll.access(2).data == 3

def test_replace():
    ll.replace(1, myfunctions.Node(10))
    assert ll.access(1).data == 10

def test_insert():
    ll.insert(4, myfunctions.Node(12))
    assert ll.access(4).data == 12

def test_delete():
    ll.delete(0)
    assert ll.count() == 6

def test_subLL():
    subLL = ll.subLL(0,2)
    assert subLL.head.data == 10



 