from avl_tree import Node, AVL_tree
import random

'''
test AVL tree
'''

# Instantiate avl
print('\n*** Instantiate avl ***\n')
avl = AVL_tree()
for i in range(50):
    avl.insert(i)


avl.print_tree(avl.root, "data")
avl.delete(31)
avl.delete(30)
avl.delete(29)

avl.print_tree(avl.root, "data")

