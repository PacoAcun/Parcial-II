'''
AVL Tree
'''

class Node:

    def __init__(self, data: int):
        """
        Initialize the node with data and children

        :param data: data to be stored in the node
        """
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

    def __repr__(self):
        return '({})'.format(self.data)

class AVL_tree:
    """
    AVL tree class.
    """

    def __init__(self):
        """
        Initialize the tree.
        """
        self.root = None

    def insert(self, data: int):
        """
        Insert a new node with data.

        :param data: data to be stored in the new node
        """
        self.root = self._insert(data, self.root)
        return self.root
    
    def _insert(self, data: int, node: Node):
        """
        Insert a new node with data into the tree.

        :param data: data to be stored in the new node
        :param node: current node
        """
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left_child = self._insert(data, node.left_child)
        else:
            node.right_child = self._insert(data, node.right_child)
        return node
    
    def delete(self, data: int):
        """
        Delete a node with data from the tree.

        :param data: data to be deleted
        """
        self.root = self._delete(data, self.root)
        return self.root
    
    def _delete(self, data: int, node: Node):
        """
        Delete a node with data from the tree.

        :param data: data to be deleted
        :param node: current node
        """
        if node is None:
            return node
        elif data < node.data:
            node.left_child = self._delete(data, node.left_child)
        elif data > node.data:
            node.right_child = self._delete(data, node.right_child)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                node.data = self.get_min(node.right_child)
                node.right_child = self._delete(node.data, node.right_child)
        return node
    
    def get_min(self, node: Node):
        """
        Get the minimum value in the tree.

        :param node: current node
        """
        while node.left_child:
            node = node.left_child
        return node.data
    
    def get_max(self, node: Node):
        """
        Get the maximum value in the tree.

        :param node: current node
        """
        while node.right_child:
            node = node.right_child
        return node.data
    
    def search(self, data: int):
        """
        Search for a node with data in the tree.

        :param data: data to be searched
        """
        return self._search(data, self.root)
    
    def _search(self, data: int, node: Node):
        """
        Search for a node with data in the tree.

        :param data: data to be searched
        :param node: current node
        """
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left_child)
        else:
            return self._search(data, node.right_child)
        
    def traverse(self, subtree: Node) -> None:
        """
        Traverse the tree.

        :param subtree: current subtree
        """
        print(subtree)

        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)

    def LL_rotation(self):
        """
        Perform a left-left rotation.
        """
        self.root = self._LL_rotation(self.root)
        return self.root
    
    def _LL_rotation(self, node: Node):
        """
        Perform a left-left rotation.

        :param node: current node
        """
        temp = node.left_child
        node.left_child = temp.right_child
        temp.right_child = node
        return temp
    
    def RR_rotation(self):
        """
        Perform a right-right rotation.
        """
        self.root = self._RR_rotation(self.root)
        return self.root
    
    def _RR_rotation(self, node: Node):
        """
        Perform a right-right rotation.

        :param node: current node
        """
        temp = node.right_child
        node.right_child = temp.left_child
        temp.left_child = node
        return temp
    
    def LR_rotation(self):
        """
        Perform a left-right rotation.
        """
        self.root = self._LR_rotation(self.root)
        return self.root
    
    def _LR_rotation(self, node: Node):
        """
        Perform a left-right rotation.

        :param node: current node
        """
        node.left_child = self._RR_rotation(node.left_child)
        return self._LL_rotation(node)
    
    def RL_rotation(self):
        """
        Perform a right-left rotation.
        """
        self.root = self._RL_rotation(self.root)
        return self.root
    
    def _RL_rotation(self, node: Node):
        """
        Perform a right-left rotation.

        :param node: current node
        """
        node.right_child = self._LL_rotation(node.right_child)
        return self._RR_rotation(node)
    
    def balance(self, node: Node):
        """
        Balance the tree.

        :param node: current node
        """
        balance = self.getbalance(node)
        if balance > 1:
            if self.getbalance(node.left_child) > 0:
                node = self.LL_rotation(node)
            else:
                node = self.LR_rotation(node)
        elif balance < -1:
            if self.getbalance(node.right_child) < 0:
                node = self.RR_rotation(node)
            else:
                node = self.RL_rotation(node)
        return node
    
    def getbalance(self, node: Node):
        """
        Get the balance of the tree.

        :param node: current node
        """
        if node is None:
            return 0
        return self.getheight(node.left_child) - self.getheight(node.right_child)
    
    def getheight(self, node: Node):
        """
        Get the height of the tree.

        :param node: current node
        """
        if node is None:
            return 0
        return max(self.getheight(node.left_child), self.getheight(node.right_child)) + 1