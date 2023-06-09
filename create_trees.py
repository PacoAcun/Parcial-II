from Binary_search_tree.binary_search_tree import Node, BinarySearchTree
from AVL_tree.avl_tree import Node, AVL_tree
from data_persistence import pickle_object, unpickle_object
import random

# Instantiate BST
print('\n*** Instantiate BST ***\n')
bst = BinarySearchTree()
print('BST object: {}'.format(bst)) # bst object
print('Current root: {}'.format(bst.root)) # empty root

# Instantiate avl
print('\n*** Instantiate avl ***\n')
avl = AVL_tree()
print('avl object: {}'.format(avl)) # avl object
print('Current root: {}'.format(avl.root)) # empty root

# Inserts
print('\n*** Inserting Nodes in Tree ***\n')
n = 10000000


for _ in range(n):
    x = random.randint(0, 1000000000000)
    bst.insert(x)
    avl.insert(x)
    

pickle_object(bst, './saved_bst')
pickle_object(avl, './saved_avl')
print('-----------Completed-----------')