from avl_tree import Node, AVL_tree

'''
test AVL tree
'''

# Instantiate avl
print('\n*** Instantiate avl ***\n')
avl = AVL_tree()
print('avl object: {}'.format(avl)) # avl object
print('Current root: {}'.format(avl.root)) # empty root


# Inserts
print('\n*** Inserting Nodes in Tree ***\n')
# n = 10
nodes_values = [33, 77, 4, 11, 16, 55, 5, 1, 14, 63]

# for _ in range(n):
#     nodes_values.append(random.randint(0, 100))

for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    avl.insert(value)

print('Current root: {}'.format(avl.root)) # current root


# Traverse
print('\n*** Traversing Tree ***\n')
avl.traverse(avl.root)


# Search 
print('\n*** Searching keys in Tree ***\n')
test_keys = [33, 44, 2, 3, 4, 63, 1]

for key in test_keys:
    print('Searching for {}: {}'.format(key, avl.search(key)))

# Min-Max 
print('\n*** Searching for min-max in Tree ***\n')
print('Min: {}'.format(avl.get_min(avl.root)))
print('Max: {}'.format(avl.get_max(avl.root)))

# Delete
print('\n*** Deleting Nodes in Tree ***\n')

for key in test_keys:
    print('Deleting node with value: {}'.format(key))
    avl.delete(key)

print('Current root: {}'.format(avl.root))

