import random
import traceback
import glog as log
""" This version is with debug logging codes"""

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


class biNode:
    """ This is a class node with which a binary search tree can be built.
    The binary search tree has the following properties:

    1. Binary tree can be built by inserting nodes or its key, or
        from a list of keys.
    2. No duplicate key is allowed.
    3. all nodes are placed with keys in an accending ("Inorder") order
    4. Each node with at most two children nodes allowed
    5. Binary tree can be converted to a list in an accending or deccending order
    6. Any node can be removed from binary tree
    7. Any subtree can be removed from binary tree
    8. The entire tree can be removed in a postorder traversal order
    9. The whole tree can be discarded recursively from the root till empty

    Errors that this module might return:

    -1: Node key duplicate
    -2: Node/key not found
    """

    # 類別變數:
    # 節點總數，初值0
    count = 0
    root = None

    # 物件實體化
    def __init__(self, value, left=None, right=None):
        self.key = value
        self.left = left
        self.right = right
        biNode.count += 1
        if biNode.count == 1:
            # first node becomes the root node
            biNode.root = self

    # Problem envountered:
    # __del__() does not always get invoked upon 'del <object>''
    # Problem workaround
    def free_node(self):
        """ delete a biNode object
    Syntax:
        <obj>.free_node()
        return 0
        """

        # unreference the node and let Python performs
        # garbage collection automatically
        self = None

        biNode.count -= 1
        if biNode.count <= 0:
            # btree is empty
            biNode.root = None
            biNode.count = 0
        return 0

    # def __del__(self):
    #     biNode.count -= 1
    #     if biNode.count == 0:
    #         # btree is empty
    #         biNode.root = None
    #     else:
    #         print(f'{get_function_name()}: root key = {biNode.root.key}')
    #         print(
    #             f'{get_function_name()}: {biNode.root.sort_keys()} with {biNode.count} node(s)\n')

    def insert_node(self, node):
        """ To insert a node into a btree, rooted by self
    Syntax:
        <obj>.insert_node(node)
        return:
             0: if successful
            -1: ignore the insertion if duplicate key
        """

        if node.key == self.key:
            # duplicated key
            return -1   # key duplicate

        if node.key < self.key:
            if self.left is None:
                self.left = node
                return 0
            else:
                if self.left.insert_node(node) == -1:
                    return -1
        else:  # i.e node.key > self.key
            if self.right is None:
                self.right = node
                return 0
            else:
                if self.right.insert_node(node) == -1:
                    return -1
        return 0

    def remove_node(self, key):
        """ To remove a node given a key within self sub-tree
    Syntax:
        <obj>.remove_node(key)
        return:
            node to remove if successfully
            -2: node/key not found
        """

        # Base Case
        if key == self.key:

            # Found the node to be removed.

            # If the node is a leaf node
            if self.left is None and self.right is None:
                log.debug(
                    f'{get_function_name()}: removing {self} with key={self.key}.')
                self.free_node()
                return self

            # If one of the children is empty
            if self.left is None:
                temp = self.right
                log.debug(
                    f'{get_function_name()}: removing {self} with key={self.key}.')
                self.free_node()
                return temp

            elif self.right is None:
                temp = self.left
                log.debug(
                    f'{get_function_name()}: removing {self} with key={self.key}.')
                self.free_node()
                return temp

            # If both children exist

            # Find Successor and its parent if any
            succParent = self
            succ = self.right

            while succ.left != None:
                succParent = succ
                succ = succ.left

            # Delete successor.Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.

            # If there is no succParent,
            # then assign succ->right to root->right (i.e. succParent == root)
            if succParent != self:
                succParent.left = succ.right
            else:
                succParent.right = succ.right

            # Copy Successor Data to root
            self.key = succ.key
            log.debug(
                f'{get_function_name()}: removing {succ} with key={succ.key}.')
            succ.free_node()

        # Recursive calls for downstream of
        # node to be removed
        else:   # Target node not found yet, recursively go left or right
            if key < self.key:

                log.debug(
                    f'{get_function_name()}: go left: {key} < {self.key}')

                # go left
                if self.left is None:
                    return -2   # node not found
                else:   # go left recursively
                    return self.left.remove_node(key)
            else:

                log.debug(
                    f'{get_function_name()}: go right: {key} > {self.key}')

                # go right
                if self.right is None:
                    return -2   # node not found
                else:   # go right recursively
                    return self.right.remove_node(key)
        return self

    def find_node(self, key):
        """Find a node given a key within self subtree
    Syntax:
        <obj>.find_node(key)
        return:
            biNode object if key is found
            -2: if not found
        """
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is None:
                log.debug(f'{get_function_name()}: key = {key} not found.')
                return -2   # key not found
            else:
                return self.left.find_node(key)
        else:  # ie key > self.key
            if self.right is None:
                log.debug(f'{get_function_name()}: key = {key} not found.')
                return -2   # key not found
            else:
                return self.right.find_node(key)

    def find_node_max(self):
        """Find the node with max key within self subtree
        and its parent and child if any
    Syntax:
        <obj>.find_node_max()
        return 3 parameters:
            1. A biNode object with the max key (ie, max-node)
            2. A parent node of the max-node if any, None otherwise
            3. A child node of the max-node if any, None otherwise
        """

        if self.right is None:   # only 1 generation
            # self has no child on the right, so self is the max-node
            if self.left is None:
                # The max-node is a really leaf node (and no parent)
                return self, None, None
            else:
                # The max-node has a child on the left
                return self, None, self.left
        else:   # self has a child on the right, looking one level down
            # checking if self has a grandchild on the right
            if self.right.right is None:   # 2 generations
                # no grandchild on the right, so self's child is the max-node
                if self.right.left is None:
                    # The max-node does not have a child on the left
                    return self.right, self, None
                else:
                    # The max-node has a child on the left
                    return self.right, self, self.right.left
            else:   # self has a grandchild on the right (3 generations)
                # self right child is not the max yet, recursively down
                return self.right.find_node_max()

    def find_node_min(self):
        """Find the node with min key within self subtree
        and its parent and child if any
    Syntax:
        <obj>.find_node_min()
        return 3 parameters:
            1. A biNode object with the min key (ie, min-node)
            2. A parent node of the min-node if any, None otherwise
            3. A child node of the min-node if any, None otherwise
        """

        if self.left is None:   # only 1 generation
            # self has no child on the left, so self is the max-node
            if self.right is None:
                # The min-node is a really leaf node (and no parent)
                return self, None, None
            else:
                # The min-node has a child on the right
                return self, None, self.right
        else:   # self has a child on the left, looking one level down
            # checking if self has a grandchild on the right
            if self.left.left is None:   # 2 generations
                # no grandchild on the left, so self's child is the min-node
                if self.left.right is None:
                    # The min-node does not have a child on the right
                    return self.left, self, None
                else:
                    # The min-node has a child on the right
                    return self.left, self, self.left.right
            else:   # self has a grandchild on the left (3 generations)
                # self left child is not the min yet, recursively down
                return self.left.find_node_min()

    def find_node_parent(self, key):
        """ Find a node given a key and its parent if any within self subtree.
    Syntax:
        <obj>.find_node_parent(node)
        return: 3 parameters
            Target biNode object with matching key value, None otherwise
            Parent biNode object if exists, None otherwise
            True: Target node is on the parent's left arm, False otherwise
            """

        if key == self.key:
            # target is the root, no parent found
            return None, None, False

        elif key < self.key:
            # check left child
            if self.left is None:
                # target not found, so no parent found either
                return None, None, False

            if key == self.left.key:
                # left child is the target, parent found
                return self.left, self, True

            else:
                # go left
                return self.left.find_node_parent(key)

        else:
            # check right child
            if self.right is None:
                # child not found, so no parent found either
                return None, None, False

            if key == self.right.key:
                # right child is the target, parent found
                return self.right, self, False

            else:
                # go right
                return self.right.find_node_parent(key)

    def print_keys(self, order):
        """ Print all the keys within self sub-tree in 3 orders
    Syntax:
        <obj>.print_keys(order)
        return:
            sorted string of keys if order = "Inorder"
            postorder string if order = "Postorder"
            preorder string if order = "Preorder"
            None: invalide order
        """

        if order == "Inorder":
            self.print_keys_inorder()

        elif order == "Postorder":
            self.print_keys_postorder()

        elif order == "Preorder":
            self.print_keys_preorder()

        else:
            print(f'Invalid order: {order}')

    def print_keys_inorder(self):

        if self.left is not None:
            self.left.print_keys_inorder()

        print(self.key, end=' ')

        if self.right is not None:
            self.right.print_keys_inorder()

    def print_keys_postorder(self):

        if self.left is not None:
            self.left.print_keys_postorder()

        if self.right is not None:
            self.right.print_keys_postorder()

        print(self.key, end=' ')

    def print_keys_preorder(self):

        print(self.key, end=' ')

        if self.left is not None:
            self.left.print_keys_preorder()

        if self.right is not None:
            self.right.print_keys_preorder()

    def sort_keys(self, reverse=False):
        """ Traverse the btree (Inorder) to retrieve keys
            in accending order (reverse=False by default) or
            in decending order (reverse=True)
    Syntax:
        <obj>.sort_keys(reverse)
        return:
            A sorted list of keys
        """
        key_list = []
        self.append_key(key_list, reverse)
        return key_list

    def append_key(self, key_list, reverse=False):
        """ Internal recursive function, invoked by sort_keys()
    Syntax:
        <obj>.append_key(node_list, reverse)
        return 0
        """

        if reverse is False:
            if self.left is not None:
                self.left.append_key(key_list, reverse)

            key_list.append(self.key)

            if self.right is not None:
                self.right.append_key(key_list, reverse)
        else:
            if self.right is not None:
                self.right.append_key(key_list, reverse)

            key_list.append(self.key)

            if self.left is not None:
                self.left.append_key(key_list, reverse)

    def sort_nodes(self, reverse=False):
        """ Traverse the btree (Inorder) to retrieve nodes
            in accending order if reverse=False (by default) or
            in decending order if reverse=True
    Syntax:
        <obj>.sort_nodes(reverse)
        return:
            A sorted list of nodes
        """

        node_list = []
        self.append_node_inorder(node_list, reverse)
        return node_list

    def append_node_inorder(self, node_list, reverse=False):
        """ Append nodes in inorder traversal manner
        i.e. left, self, right order
    Syntax:
        <obj>.append_node_inorder(node_list, reverse)
        return 0
        """

        if reverse is False:
            if self.left is not None:
                self.left.append_node_inorder(node_list, reverse)

            node_list.append(self)

            if self.right is not None:
                self.right.append_node_inorder(node_list, reverse)

        else:   # ie in reverse order
            if self.right is not None:
                self.right.append_node_inorder(node_list, reverse)

            node_list.append(self)

            if self.left is not None:
                self.left.append_node_inorder(node_list, reverse)

        return 0

    def append_node_postorder(self, node_list):
        """ Append nodes in a postorder traversal manner
        i.e. left, right and self ordr
    Syntax:
        <obj>.append_postorder(node_list)
        return 0
        """

        if self.left is not None:
            self.left.append_node_postorder(node_list)

        if self.right is not None:
            self.right.append_node_postorder(node_list)

        node_list.append(self)

    def append_node_preorder(self, node_list):
        """ Append nodes in a preorder traversal manner
        i.e. self, left, right ordr
    Syntax:
        <obj>.append_postorder(node_list)
        return 0
        """

        node_list.append(self)

        if self.left is not None:
            self.left.append_node_preorder(node_list)

        if self.right is not None:
            self.right.append_node_preorder(node_list)

    def remove_tree(self):
        """ Free up all nodes within self subtree by removing all the nodes
        with leaf node first, i.e. in a postorder traversal manner.
    Syntax:
        <obj>.remove_tree()
        return: 0
        """

        # if self is not the root, we need to
        # cut the subtree out of main tree prior to removal.
        node_found, node_p, from_left = biNode.root.find_node_parent(self.key)

        if node_p is not None:
            if from_left:
                node_p.left = None
            else:
                node_p.right = None

        list_stack = []
        self.append_node_postorder(list_stack)

        for node in list_stack:
            log.debug(
                f'{get_function_name()}: leaf found with key={node.key}.')
            self.remove_node(node.key)

        return 0

    @classmethod
    def insert_tree(cls, key):

        # If the tree is empty,
        # return a new node
        if biNode.root is None:
            return biNode(key)

        # Otherwise check any node with the key down the tree
        node_found = biNode.root.find_node(key)
        if node_found == -2:
            # create a new node
            node_new = biNode(key)

            # insert new node into btree
            biNode.root.insert_node(node_new)
            return node_new
        else:
            # return node that already exist with the same key
            return node_found

    @classmethod
    def discard_tree(cls):
        """ Free up all the nodes within the whole btree from the root first
        till the btree is empty
    Syntax:
        biNode.discard_tree()
        return: 0
        """

        if cls.root is None:
            return 0
        else:
            cls.root.remove_node(biNode.root.key)

        if cls.root is not None:
            return cls.root.discard_tree()
        else:
            return 0


if __name__ == '__main__':
    """ Example code, demonstrating:
        Build a binary tree with random numbers
        1. Plus root node with key of 500
        2. With keys of 9 random-number keys between 100 and 999
        3. Showing btree in 3 orders
        4. Converting btree to a sorted list in accending order
        5. Converting btree to a sorted list in decending order
        6. Removing the whole tree
    """

    log.setLevel("DEBUG")
    node_root = biNode.insert_tree(500)
    print(
        f'Example 1: Binary Tree root at {node_root} with key = {node_root.key}\n')

    for _ in range(9):
        bn = biNode.insert_tree(random.randint(100, 999))
        print(f'Example 2: Node at {bn} inserted with key = {bn.key}')
    print()

    print(f'Example 3: Number of nodes in btree = {biNode.count}')
    print(f'Example 3.1: printing keys Inorder:')
    node_root.print_keys("Inorder")
    print('\n')

    print(f'Example 3.2: printing keys Postorder:')
    node_root.print_keys("Postorder")
    print('\n')

    print(f'Example 3.3: printing keys Preorder:')
    node_root.print_keys("Preorder")
    print('\n')

    # Converting binary tree to list
    new_list = node_root.sort_keys()
    print(f'Example 4: sorted key-list:\n {new_list}\n')
    rev_list = node_root.sort_keys(reverse=True)
    print(f'Example 5: reverse-sorted key-list:\n {rev_list}\n')

    # Discard the whole tree
    print(
        f'Example 6: Discarding btree, root at {biNode.root} with key = {biNode.root.key}')
    biNode.discard_tree()
    print(f'Example 6: The whole tree discarded. Program terminated.')
