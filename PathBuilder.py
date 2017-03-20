# -*- coding: utf-8 -*-
"""
Created on Mon Mar  20 17:00:30 2017

@author: wsdula
"""

NullVec = []
n = int(input("How long are the paths? "))
a = int(input("What area are the paths? "))

class TreeObj(object):
    "tree definition"
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self):
        assert isinstance(node, TreeObj)
        self.children.append(node)
        
dyck = TreeObj(NullVec, )