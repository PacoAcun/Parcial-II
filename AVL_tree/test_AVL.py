from avl_tree import Node, AVL_tree
import random

'''
test AVL tree
'''

# Instantiate avl
print('\n*** Instantiate avl ***\n')
avl = AVL_tree()
for i in range(100):
    x = random.randint(0, 100)
    avl.insert(i)


avl.print_tree(avl.root, "data")
#avl.delete(63)
#print(avl.search(90))
#print(avl.search(143))

#for i in range(80):
    #avl.delete(i)




