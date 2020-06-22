#will not run until implement files
#first attempt

from LinkedList import LinkedList #need to implement to run (1/2)
from Node import Node #need to implement to run (2/2)

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    if lst.head_node is None:
        return False
    currNode = lst.head_node
    node2del = None
    while currNode:
        if currNode.data == value:
            node2del = currNode
            currNode = currNode.next_element
            node2del = None
            return True
        currNode = currNode.next_element
    
    #traversed to end and val not found
    return False