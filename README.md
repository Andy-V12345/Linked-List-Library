# Linked List Library
A Python library that provides useful functions for linked lists
## Installation
Download the files and in the terminal, cd into the root folder
```bash
cd /path/to/Linked-List-Library
```
Create a wheelfile.whl file
```bash
python setup.py bdist_wheel
```
The wheel file is stored in the newly created "dist" folder". Install the library
 ```bash
 pip install /path/to/wheelfile.whl
 ```
 ## Usage
 ```python
 from LinkedListFunctionsLib import myfunctions
 
 # creates a linked list from a normal list
 aList = [1, 2, 3, 4]
 ll = myfunctions.createLL(aList)
 
 # returns the length of a linked list
 ll.count()
 
 # returns the node at a specified index
 ll.access(2)
 
 # replaces a node at a specified index with another node
 ll.replace(1, Node(5))
 
 # inserts a new node at a specified index
 ll.insert(2, Node(6))
 
 # deletes the node at a specified index
 ll.delete(2)
 
 # prints out every node in the linked list
 ll.print()
 ```
 
