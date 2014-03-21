__author__ = 'clh'

class PunGraph:

    def __init__(self):
        self.score = None
        self.nodes = []
        self.edges = []

    #Computes the Pun score for the Graph, by traversing all the nodes and edges.
    def compute_score(self):
        score = 0
        for edge in self.edges:
            score += edge.score
        for node in self.nodes:
            score += node.score
        return score

    #Getter for the Pun Score of this graph. Computes if not already set.
    def score(self):
        if self.score is None:
            self.score = self.compute_score
        return self.score

    #Print the graph to a terminal
    def to_string(self):
        pass

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)
