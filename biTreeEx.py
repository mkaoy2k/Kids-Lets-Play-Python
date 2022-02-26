
from biTree import biNode

""" Example code, demonstrating:
    1. Build a binary tree from a list of integers
    2. Showing btree info:
        1) print_keys()
        2} sort_keys()
    3. finding out max and min keys of the btree
    4. finding a node given a key
    5. removing a node given a key
    6. Discarding the whole tree
"""

numbers = [5, 4, 1, 9, 5, 3, 7, 6, 8, 2]
print(f'Number of items in {numbers} = {len(numbers)}\n')

# create root of binary tree
node_root = biNode(numbers.pop())

# To iterate from the second element to the end
for key in numbers:
    bn = biNode(key)
    if node_root.insert_node(bn) == -1:
        print(f'duplicated key = {bn.key}\n')
        bn.free_node()

# print the sorted keys
print(f'printing keys:', end=' ')
node_root.print_keys()
print()

# To print the sorted keys in a list
print(
    f'sorting keys: {biNode.root.sort_keys()} with {biNode.count} node(s)')
print(f'root key of the btree = {biNode.root.key}')

# To print the max node and key
node_max = node_root.find_node_max()
print(f'maximum key of the btree = {node_max.key}')

# To print the min node and key
print(f'minimum key = {node_root.find_node_min().key}\n')

# Example: To find a node from btree given a key
key = 7
node = node_root.find_node(key)
if node != -2:
    print(f'node type: {type(node)} = {node}')
    print(f'node.key= {node.key}')

# Example: To remove a node from btree given a key
key = 8
# find the node with the key
# return -2 if key not found
node_target = node_root.find_node(key)
if node_target == -2:
    print(f'key= {key} not found.\n')
else:
    if node_root.remove_node(node_target) == 0:
        print(f'key= {key} removed successfully.\n')
        print(f'{node_root.sort_keys()} with {biNode.count} node(s)')
        print(f'root key of the btree = {node_root.key}\n')
    else:
        print(f'key= {key} remove_node() failed.\n')

# Discarding the whole tree
biNode.root.discard_tree()
print(f'Discard the whole tree. Program terminated.')
