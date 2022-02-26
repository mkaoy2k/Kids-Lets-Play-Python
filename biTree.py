import random
import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


class biNode:
    """ This is a class node for building a binary tree
    which has the following properties::
    1. Binary tree can be built by inserting nodes or from a list
    2. all nodes are sorted with keys in asscending order
    3. Each node with at most two children nodes is allowed
    3. Binary tree can be converted to a list in an accending or deccending order
    4. Any node can be removed from binary tree

    Errors that this module might return:

    -1: Node key duplicate
    -2: Node key not found
    -3: Root node not found
    -4: Unknown error
    -5: Parent node can not be located
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

        <obj>.free_node()
        return 0
        """

        del self
        biNode.count -= 1
        if biNode.count == 0:
            # btree is empty
            biNode.root = None
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

    def remove_node(self, node):
        """ To remove a node from btree, rooted from self

        <ogj>.remove_node(node)
        return:
             0: remove successfully
            -4: unknown error
        """

        # Approach: 2 cases that could happen
        # 1. root case
        # 2. non-root case
        # case 1: remove root node
        if node.key == biNode.root.key:
            node_target = biNode.root

            # make the left child as root if not empty
            if node_target.left is not None:
                biNode.root = node_target.left

                # prepare right tree to merge
                if node_target.right is None:
                    nodes_list = []
                else:
                    nodes_list = node_target.right.sort_nodes()

            # make the right child as root if not empty
            elif node_target.right is not None:
                biNode.root = node_target.right

                # prepare left tree to merge
                if node_target.left is None:
                    nodes_list = []
                else:
                    nodes_list = node_target.left.sort_nodes()

            # Lastly, root does not have any child
            else:
                # update class variable root
                biNode.root = None

                # no merge trees necessary
                nodes_list = []

        else:
            # case 2: find out the node's parent existed in the btree
            node_parent, node_target, from_left = biNode.root.find_dad_kid(
                node.key)
            if node_parent == -5:
                return -5
            if node_parent == -4:
                return -4

            # checking target node is from left or right of parent
            if from_left:
                # cut the target subtree off the parent
                node_parent.left = None
            else:
                # cut the target subtree off the parent
                node_parent.right = None

            # collect left subtree into merge list
            if node_target.left is None:
                nodes_left = []
            else:
                nodes_left = node_target.left.sort_nodes()

            # collect right subtree into merge list
            if node_target.right is None:
                nodes_right = []
            else:
                nodes_right = node_target.right.sort_nodes()

            nodes_list = nodes_left + nodes_right

        # print(f'{get_function_name()}: nodes list = {nodes_list}')

        # free target node
        node_target.free_node()

        # re-insert all the nodes of merge list back to the new btree
        for node in nodes_list:
            node.left = None
            node.right = None
            # print(f'{get_function_name()}: insert key = {node.key}')

            if biNode.root.insert_node(node) != 0:
                return -4

        # # trace logging
        # if biNode.count > 0:
        #     print(f'{get_function_name()}: root key = {biNode.root.key}')
        #     print(
        #         f'{get_function_name()}: {biNode.root.sort_keys()} with {biNode.count} node(s)\n')
        return 0

    def find_dad_kid(self, key):
        """ From self (normally root) node, to find parent of the node given a key

        <obj>.find_dad_kid(key)
        return:
            3 parameters
                2 biNodes, Dad and kid objects, given kid's key
                1 boolean, indicating kid's node from left arm of parent's or not
            -5: if parent node can not be found
            -4: unknown error
        """

        # no parent could be found
        if key == self.key:
            # print(f'{get_function_name()}: parent node can not be found.')
            return -5   # parent can not be found

        if key < self.key:
            if self.left is None:
                # print(f'{get_function_name()}: parent node can not be found.')
                return -5   # parent can not be found
            else:   # ie have a left child
                if key == self.left.key:
                    return self, self.left, True   # found
                else:
                    return self.left.find_dad_kid(key)
        else:   # ie key > self.key
            if self.right is None:
                # print(f'{get_function_name()}: parent node can not be found.')
                return -5   # parent can not be found
            else:   # ie have a right child
                if key == self.right.key:
                    return self, self.right, False   # found
                else:
                    return self.right.find_dad_kid(key)
        # print(f'{get_function_name()}: unknown error.')
        return -4   # unknown error

    def find_node(self, key):
        """From self node, to find a node given a key

        <obj>.find_node(key)
        return:
            biNode object if key is found
            -2: if not found
        """
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is None:
                return -2   # key not found
            else:
                return self.left.find_node(key)
        else:  # ie key > self.key
            if self.right is None:
                return -2   # key not found
            else:
                return self.right.find_node(key)

    def find_node_max(self):
        """From self node, find the node with max key
        <obj>.find_node_max()
        return:
            biNode object with the max key
        """
        if self.right is None:
            return self
        else:
            return self.right.find_node_max()

    def find_node_min(self):
        """From self node, find the node with min key

        <obj>.find_node_min()
        return:
            biNode object with the min key
        """

        if self.left is None:
            return self
        else:
            return self.left.find_node_min()

    def print_keys(self):
        """ Print the keys within the btree, rooted by self

        <obj>.print_keys()
        return:
            sorted list of keys within the subtree from self node
        """

        if self.left is not None:
            self.left.print_keys()

        print(self.key, end=' ')

        if self.right is not None:
            self.right.print_keys()

    def sort_keys(self, reverse=False):
        """ Traverse the btree (Inorder) to retrieve keys
            in accending order (reverse=False by default) or
            in decending order (reverse=True)

        <obj>.sort_keys(reverse)
        return:
            A sorted list of keys
        """
        key_list = []
        self.append_key(key_list, reverse)
        return key_list

    def append_key(self, key_list, reverse=False):
        """ Internal recursive function, invoked by sort_keys()

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
            in accending order (reverse=False by default) or
            in decending order (reverse=True)

        <obj>.sort_nodes(reverse)
        return:
            A sorted list of nodes
        """

        node_list = []
        self.append_node(node_list, reverse)
        return node_list

    def append_node(self, node_list, reverse=False):
        """ Internal recursive function, invoked by sort_nodes()

        <obj>.append_node(node_list, reverse)
        return 0
        """

        if reverse is False:
            if self.left is not None:
                self.left.append_node(node_list, reverse)

            node_list.append(self)

            if self.right is not None:
                self.right.append_node(node_list, reverse)
        else:   # ie in reverse order
            if self.right is not None:
                self.right.append_node(node_list, reverse)

            node_list.append(self)

            if self.left is not None:
                self.left.append_node(node_list, reverse)

        return 0

    def discard_tree(self):
        """ Discard the whole tree, rooted by self,
        by removing all the nodes out of btree

        <obj>.discard_tree()
        return: 0
        """

        while self.left is not None:

            # # tracing
            # print(
            #     f'{get_function_name()}: discarding node with key = {self.left.key}')
            self.remove_node(self.left)
            # print(
            #     f'{get_function_name()}: {biNode.root.sort_keys()} with {biNode.count} node(s)')

        while self.right is not None:

            # # tracing
            # print(
            #     f'{get_function_name()}: discarding node with key = {self.right.key}')
            self.remove_node(self.right)
            # print(
            #     f'{get_function_name()}: {biNode.root.sort_keys()} with {biNode.count} node(s)')

        self.remove_node(self)

        return 0


if __name__ == '__main__':
    """ Example code, demonstrating:
        Build a binary tree with random numbers
        1. With keys of 9 random-number keys between 100 and 999
        2. Plus root node with key of 500
        3. Showing btree info
        4. Converting btree to a sorted list in accending order
        5. Converting btree to a sorted list in decending order
        6. Discrding the whole tree
    """

    node_root = biNode(500)
    print(f'Binary Tree with root.key = {node_root.key}')

    for _ in range(9):
        bn = biNode(random.randint(100, 999))
        if node_root.insert_node(bn) == -1:
            print(f'duplicated key = {bn.key}\n')
            bn.free_node()  # duplicate

    print(f'Number of nodes = {biNode.count}\n')
    print(f'printing keys:')
    node_root.print_keys()
    print('\n')

    # Converting binary tree to list
    new_list = node_root.sort_keys()
    print(f'sorted key-list:\n {new_list}\n')
    rev_list = node_root.sort_keys(reverse=True)
    print(f'reverse-sorted key-list:\n {rev_list}\n')

    # Discard the whole tree
    biNode.root.discard_tree()
    print(f'Discard the whole tree. Program terminated.')
