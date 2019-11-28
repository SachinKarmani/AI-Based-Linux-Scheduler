from Process import Process

BLACK = 1
RED = 0
NIL = None


class Node:
    def __init__(self, process, color, parent=None, left=None, right=None):
        self.process = process
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        if self.process == None:
           val = 'N'
        else:
            val = self.process.processId
        return str(val)

    def __iter__(self):
        if self.left.color != NIL:
            yield from self.left.__iter__()

        yield self.value

        if self.right.color != NIL:
            yield from self.right.__iter__()

    # def __eq__(self, other):
    #     if self.color == NIL and self.color == other.color:
    #         return True
    #
    #     if self.parent is None:
    #         if other.parent is None:
    #             parents_are_same = self.parent is None and other.parent is None
    #     else:
    #         parents_are_same = self.parent.value == other.parent.value and self.parent.color == other.parent.color
    #     return self.value == other.value and self.color == other.color and parents_are_same

    def has_children(self) -> bool:
        """ Returns a boolean indicating if the node has children """
        return bool(self.get_children_count())

    def get_children_count(self) -> int:
        """ Returns the number of NOT NIL children the node has """
        if self.color == NIL:
            return 0
        return sum([int(self.left.color != NIL), int(self.right.color != NIL)])




class RedBlackTree:
    # every node has null nodes as children initially, create one such object for easy management
    NIL_LEAF = Node(process=None, color=BLACK, parent=None)

    def __init__(self):
        self.count = 0
        self.root = self.NIL_LEAF

    def add(self, process):

        new_node = Node(process, parent=self.NIL_LEAF,left=self.NIL_LEAF, right=self.NIL_LEAF,color = BLACK )

        if self.root.process == None:
            new_node.color = BLACK
            self.root = new_node
            self.count += 1
            return

        new_node.color = RED
        temp = self.root

        while(True):

            if (new_node.process.unfairness < temp.process.unfairness):
                if(temp.left == self.NIL_LEAF):
                    temp.left = new_node
                    new_node.parent = temp
                    break
                else:
                    temp = temp.left

            else:
                if(temp.right == self.NIL_LEAF):
                    temp.right = new_node
                    new_node.parent = temp
                    break
                else:
                    temp = temp.right


        # parent, node_dir = self._find_parent(value)
        # if node_dir is None:
        #     return  # value is in the tree
        # new_node = Node(value=value, color=RED, parent=parent,
        #                 left=self.NIL_LEAF, right=self.NIL_LEAF)
        # if node_dir == 'L':
        #     parent.left = new_node
        # else:
        #     parent.right = new_node

        self._try_rebalance(new_node)
        self.count += 1

    def _try_rebalance(self, node):
        """
        Given a red child node, determine if there is a need to rebalance (if the parent is red)
        If there is, rebalance it
        """

        while(node.parent.color == RED):
            uncle = self.NIL_LEAF

            if (node.parent == node.parent.parent.left):
                uncle = node.parent.parent.right

                if (uncle != self.NIL_LEAF and uncle.color == RED):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                    continue

                if (node == node.parent.right):
                    node = node.parent
                    self.rotateLeft(node)

                node.parent.color = BLACK
                node.parent.parent.color = RED

                self.rotateRight(node.parent.parent)

            else:
                uncle = node.parent.parent.left
                if (uncle != self.NIL_LEAF and uncle.color == RED):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                    continue

                if (node == node.parent.left):
                    node = node.parent
                    self.rotateRight(node);


                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.rotateLeft(node.parent.parent)


        self.root.color = BLACK;

    def printRBTree(self):

        self.printTree(self.root)

    def printTree(self, node):

        if node == self.NIL_LEAF:
            return

        self.printTree(node.left)
        print("ID: ", node.process.processId, '\t',
              "Exec: ", round(node.process.execTime,2), '\t',
              "VrunTime: ", round(node.process.unfairness,2), '   ', 
              "Arrival: ", node.process.arrivalTime, '\t',
              "Color: ", ('B' if node.color == 1 else 'R'), '\t',
              "Parent: ", node.parent,'\t',
              "Left: ",  node.left, '\t',
              "Right ", node.right
              )
        self.printTree(node.right)






    def rotateLeft(self, node):
        if (node.parent != self.NIL_LEAF):
            if (node == node.parent.left):
                node.parent.left = node.right
            else:
                node.parent.right = node.right

            node.right.parent = node.parent
            node.parent = node.right
            if (node.right.left != self.NIL_LEAF):
                node.right.left.parent = node

            node.right = node.right.left
            node.parent.left = node

        else:
            ## Need to rotate root
            right = self.root.right;
            self.root.right = right.left
            right.left.parent = self.root
            self.root.parent = right
            right.left = self.root
            right.parent = self.NIL_LEAF
            self.root = right;

    def rotateRight(self, node):

        if (node.parent != self.NIL_LEAF):
            if (node == node.parent.left):
                node.parent.left = node.left
            else:
                node.parent.right = node.left

            node.left.parent = node.parent
            node.parent = node.left
            if (node.left.right != self.NIL_LEAF):
                node.left.right.parent = node

            node.left = node.left.right
            node.parent.right = node

        else:
            ## Need to rotate root
            left = self.root.left;
            self.root.left = self.root.left.right
            left.right.parent = self.root
            self.root.parent = left
            left.right = self.root
            left.parent = self.NIL_LEAF
            self.root = left;

    def findLeftMost(self):

        if self.root == self.NIL_LEAF:
            return None

        temp = self.root
        while(temp.left != self.NIL_LEAF):
            temp = temp.left

        return temp

    def treeMinimum(self, node):

        temp = node

        while(temp.left != self.NIL_LEAF):
            temp = temp.left

        return temp


    def swap(self,node1, node2):

        if (node1.parent == self.NIL_LEAF):
            self.root = node2
        elif(node1 == node1.parent.left):
            node1.parent.left = node2
        else:
            node1.parent.right = node2

        node2.parent = node1.parent

    def delete_node(self):

        node = self.findLeftMost()
        if node == None or node == self.NIL_LEAF:
            return None

        temp = node
        color = node.color

        if (node.left == self.NIL_LEAF):
            x = node.right
            self.swap(node, node.right)
        elif (node.right == self.NIL_LEAF):
            x = node.left
            self.swap(node, node.left)
        else:
            temp = self.treeMinimum(node.right)
            color = temp.color
            x = temp.right
            if (temp.parent == node):
                x.parent = temp
            else:
                self.swap(temp, temp.right)
                temp.right = node.right
                temp.right.parent = temp

            self.swap(node, temp)
            temp.left = node.left
            temp.left.parent = temp
            temp.color = node.color

        if (color == BLACK):
            self.deleteFixup(x)
        self.count -= 1
        return node


    def deleteFixup(self, x):

        while (x != self.root and x.color == BLACK):
            if (x == x.parent.left):
                w = x.parent.right
                if (w.color == RED):
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateLeft(x.parent)
                    w = x.parent.right

                if (w.left.color == BLACK and w.right.color == BLACK):
                    w.color = RED
                    x = x.parent
                    continue

                elif (w.right.color == BLACK):
                    w.left.color = BLACK
                    w.color = RED
                    self.rotateRight(w)
                    w = x.parent.right

                if (w.right.color == RED):
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.rotateLeft(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if (w.color == RED):
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateRight(x.parent)
                    w = x.parent.left

                if (w.right.color == BLACK and w.left.color == BLACK):
                    w.color = RED
                    x = x.parent
                    continue

                elif (w.left.color == BLACK):
                    w.right.color = BLACK
                    w.color = RED
                    self.rotateLeft(w)
                    w = x.parent.left

                if (w.left.color == RED):
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.rotateRight(x.parent)
                    x = self.root

        x.color = BLACK
