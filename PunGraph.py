__author__ = 'clh'

class PunGraph:

    def __init__(self):
        self.score = None

    #Computes the Pun score for the Graph, by traversing all the nodes and edges.
    def compute_score(self):
        pass

    #Getter for the Pun Score of this graph. Computes if not already set.
    def score(self):
        if self.score is None:
            self.score = self.compute_score
        return self.score

    #Print the graph to a terminal
    def to_string(self):
        pass
