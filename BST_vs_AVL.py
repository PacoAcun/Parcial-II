from Binary_search_tree.binary_search_tree import Node, BinarySearchTree
from AVL_tree.avl_tree import Node, AVL_tree
from data_persistence import pickle_object, unpickle_object
import random
import time

print('Unpicking trees....')
bst_unpick = unpickle_object('./saved_bst')
avl_unpick = unpickle_object('./saved_avl')

print(avl_unpick.root.height)



# Search
print('\n*** Searching ***\n')
search_values = []

for _ in range(5000000):
    x = random.randint(0, 1000000000)
    search_values.append(x)

start = time.time()
for value in search_values:
    bst_unpick.search(value)

end = time.time()
bst_time = end - start
print()

start = time.time()
for value in search_values:
    avl_unpick.search(value)

end = time.time()
avl_time = end - start
print('-------------------------------------------------------------')
print('BST ejecution time...: {}'.format(bst_time))
print('-------------------------------------------------------------')
print('AVL ejecution time...: {}'.format(avl_time))
print('-------------------------------------------------------------')
