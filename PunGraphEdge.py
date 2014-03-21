__author__ = 'clh'

#This is a class which would normally be inherited from.
#todo: how to do abstract class in python?

class PunGraphEdge:

    def __init__(self, graph, node1, node2):
        #a reference to the owning graph
        self.graph = graph
        self.node1 = node1
        self.node2 = node2
        self.score = None
        #finally, tell the owning graph about this edge
        self.graph.add_edge(self)

    def first_node(self):
        return self.node1

    def second_node(self):
        return self.node2

    def score(self):
        if self.score is None:
            self.score = self.compute_score
        return self.score

    def compute_score(self):
        return 0


    #todo destructor
