from typing import Any
from typing import Callable
from binarytree import build2, build
from itertools import chain


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.lista = []
        self.lista1 = []

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left_child and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)
        self.lista.append(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)
        self.lista.append(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)

        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def printnode(self):
        if self.value is not None:
            print(self.value)

    def li(self):
        return self.lista

    def zwroc_liste(self, wartosci=[]):
        if self.lista:
            for i in self.lista:
                wartosci.append(i)
        if self.left_child:
            self.left_child.zwroc_liste(wartosci)
        if self.right_child:
            self.right_child.zwroc_liste(wartosci)
        return wartosci


class BinaryTree:

    def __init__(self, value: Any):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def zwroc_liste_drzewa(self):
        return self.root.zwroc_liste()

    def show(self):
        print(build([tree.root.value] + tree.zwroc_liste_drzewa()))


def Level(node, value, level):
    if node is None:
        return 0
    if node.value is value:
        return level
    lower_level = Level(node.left_child, value, level + 1)
    if lower_level != 0:
        return lower_level
    lower_level = Level(node.right_child, value, level + 1)
    return lower_level


def horizontal_sum(tree: BinaryTree, zakres):
    result = []
    lev = 0
    poz = 0
    for x in range(zakres):
        if lev < Level(tree.root, x, 1):
            lev = Level(tree.root, x, 1)
    for n in range(0, lev):
        tmp = 0
        for i in range(1, zakres):
            if lev - poz == Level(tree.root, i, 1):
                tmp = tmp + i
        result.append(tmp)
        poz += 1
    result.reverse()
    return result


tree = BinaryTree(10)
tree.root.add_right_child(2)
tree.root.add_left_child(9)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)
print(tree.root.left_child.lista)

print(horizontal_sum(tree, 100))
print(tree.show())
#print("reczna lista")
#values = [ 9, 2, 3, 4,None,None, 6]
#print(build([9, 2, 1, None, 4, 6, None, None]))
#print(build(tree.root.value))

