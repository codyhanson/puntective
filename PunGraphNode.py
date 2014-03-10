__author__ = 'clh'


class PunGraphNode:

    def __init__(self):
        self.neighbors = {}

    def connect_node(self, edge, node):
        self.neighbors[node].append(edge)
