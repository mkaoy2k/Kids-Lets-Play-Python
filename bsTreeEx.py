from bsTree import biNode
import glog as log

""" Example code, demonstrating:
    1. Build a binary tree from a list of integers
    2. Showing btree info:
        1) print keys in "Inorder" order
        2) print keys in "Postorder" order
        3) print keys in "Preorder" order
        4} sort keys stored in a list
    3. Finding out
        1) max node of the btree
        2) min node of the btreetree
        3) max node of a sub-tree
        4) min node of a sub-tree
    4. Finding a node given a key
        1) finding a node with matching key
        2) finding target node with matching key and its parent if any
    5. Removing a node given a key
    6. Removing a subtree
    7. Removing an entire tree
"""

# log.setLevel("DEBUG")
numbers = [30, 70, 20, 40, 60, 80, 80, 50]
print(f'Number of items in {numbers} = {len(numbers)}\n')

# create root of binary tree
node_root = biNode.insert_tree(numbers.pop())
print(f'Example 1: Built a binary tree with root key = {biNode.root.key}')

# To iterate from the rest elements in the list
for key in numbers:
    bn = node_root.insert_tree(key)
    print(f'Example 1: Node at {bn} inserted with key = {bn.key}')
print()

# print keys
print(f'Example 2.1: printing keys Inorder:', end=' ')
node_root.print_keys("Inorder")
print()
print(f'Example 2.2: printing keys Postorder:', end=' ')
node_root.print_keys("Postorder")
print()
print(f'Example 2.3: printing keys Preorder:', end=' ')
node_root.print_keys("Preorder")
print()

# To print the sorted keys in a list
print(
    f'Example 2.4: sorting keys of the whole btree: {biNode.root.sort_keys()} with {biNode.count} node(s)')
print(f'root at {biNode.root} with key = {biNode.root.key}\n')

# To print the max node and key
node_max, _, _ = node_root.find_node_max()
print(f'Example 3.1: global maximum key = {node_max.key} at {node_max}')

# To print the min node and key
node_min, _, _ = node_root.find_node_min()
print(f'Example 3.2: global mainimum key = {node_min.key} at {node_min}\n')

# Example: To find a node from btree given a key
key = 30
node_found = node_root.find_node(key)
if node_found != -2:
    node_max, _, _ = node_found.find_node_max()
    print(
        f'Example 3.3: Subtree of {key} has a local maximum key = {node_max.key} at {node_max}')
    node_min, _, _ = node_found.find_node_min()
    print(
        f'Example 3.4: Subtree of {key} has a local minimum key = {node_min.key} at {node_min}\n')
    print(f'Example 4.1: Finding target node with key = {key}')
    print(f'---> Found {node_found} with key= {node_found.key}\n')

else:
    print(f'---> key = {key} not found\n')

key = 30
print(f'Example 4.2: Finding a node with key = {key} and its parent if any')
node_found, node_p, from_left = node_root.find_node_parent(key)
if node_found is None:
    print(f'---> key = {key} not found.')
    if node_p is None:
        print(f'---> parent node not found.\n')
    else:
        print(f'---> Found parent {node_p} with key= {node_p.key}\n')
else:
    print(f'---> Found target {node_found} with key= {node_found.key}')
    if node_p is None:
        print(f'---> parent node not found.\n')
    else:
        print(f'---> Found parent {node_p} with key= {node_p.key}\n')

# Example: To remove a node from btree given a key
key = 50
print(f'Example 5: Removing target node with key = {key}')

node_removed = node_root.remove_node(key)
if node_removed == -2:
    print(f'key = {key} not found.\n')
else:
    print(f'node at {node_removed} with key = {key} removed successfully.')
    print(f'{biNode.root.sort_keys()} with {biNode.count} node(s)')
    print(f'root at {biNode.root} with key = {biNode.root.key}\n')

# Removing a subtree
key = 70
node_found = node_root.find_node(key)
if node_found == -2:   # not found
    print(f'Example 6: Removing a sub-btree, invalid key = {key}\n')
else:
    print(
        f'Example 6: Removing a sub-btree of {node_found.key} at {node_found}')
    node_found.remove_tree()
    print(f'{biNode.root.sort_keys()} with {biNode.count} node(s)\n')

# Removing the entire tree
print(
    f'Example 7: Removing an entire btree, root at {biNode.root} with key = {biNode.root.key}')
node_root.remove_tree()
if biNode.root is None and biNode.count == 0:
    print(f'The entire tree removed. Program terminated.')
