#!/usr/bin/env python

import time

WAYS = []
goal=200
valueLUT = [200, 100, 50, 20, 10, 5, 2, 1]
dict_template = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}
COUNT = 0


class Tree(object):
    def __init__(self, value=0, total=0, parent=None, children=[]):
        self.value=value
        self.total=total
        self.parent=parent
        self.children=children
        self.count=0

    def add_child(self,node):
        assert isinstance(node, Tree)
        self.children.append(node)

def getCombination(node):
    new_dict = dict_template.copy()
    search_node = node

    while search_node.parent != None:
        new_dict[search_node.value] += 1
        search_node = search_node.parent

    search_node.count += 1

def genTree(node, LUT):
    for i in range(0, len(LUT)):
        if node.total + LUT[i] > goal:
            continue

        new_node = Tree(LUT[i], node.total+LUT[i], node)
        node.add_child(new_node)

        if node.total + LUT[i] < goal:
            genTree(new_node, LUT[i:])
        elif node.total + LUT[i] == goal:
            getCombination(new_node)


start = time.clock()

root = Tree()

genTree(root, valueLUT)

print(root.count)
end = time.clock()
print(end-start)
