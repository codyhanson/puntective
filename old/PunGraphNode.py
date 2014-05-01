__author__ = 'clh'


class PunGraphNode:

    def __init__(self, graph, neighbors):
        #a reference to the owning graph
        self.graph = graph
        self.score = None
        #finally, tell the owning graph about this edge
        self.graph.add_node(self)
        #dictionary keyed by edges, values are nodes.
        self.neighbors = {}
        #neighbors is a list of 2-tuples, where each 2-tuple is an edge and a node to be connected.
        for neighbor in neighbors:
            self.connect_neighbor(neighbor)

    def connect_neighbor(self, edge_node_tuple):
        pass

    def edges(self):
        return self.neighbors.keys

    #return a list of connected nodes
    def neighbor_nodes(self):
        pass

    def score(self):
        if self.score is None:
            self.score = self.compute_score
        return self.score

    def compute_score(self):
        return 0

    #todo Destructor
