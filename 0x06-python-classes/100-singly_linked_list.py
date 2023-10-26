#!/usr/bin/python3
"""This module defines a class 'Node'

The class defines a node of singly linked list
"""


class Node:
    """This class defines a node of a singly linked list

    Attributes:
        data (int): an integer

    """
    def __init__(self, data, next_node=None):
        """Initialize this node with a private data attr

        Args:
            data (int): must be an integer
            next_node (:obj: `Node`): next node in the list

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrives the data in the node

        the data is retrieve from the setter which sets teh value
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """retrieves the next node in the list

        the setter sets the value, sets head (Node) to be value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """this class defines a singly linked list

    Attributes:
        head (:obj: `Node`): receives the head of a Node
    """
    def __init__(self):
        """Initialize the head node to None

        Args:
            head (:obj: `Node`)
        """
        self.head = None

    def sorted_insert(self, value):
        """this sorts the nodes

        it also inserts values in the right position
        Args:
            value (int): the node's value

        """
        new_node = Node(value)
        # case empty list? insert node at the head
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Find the node before the place to insert
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
                # insertion
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """This prints out the data in each node

        Args:
            None
        """
        result = []  # initializes an empty list
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return "\n".join(map(str, result))
