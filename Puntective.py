import homophone
import hyphenations
import definition_linkage
import part_of_speech
from py2neo import neo4j, node, rel


class Puntective:
    def __init__(self, phrase):
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
        #empty out the database
        self.graph_db.clear()
        self.phrase = phrase

    def parse(self):
        #split the phrase into words, and add them as phrase nodes
        previous_node = None
        p = 0
        for word in self.phrase.split():
            p += 1
            if previous_node is not None:
                #add word as a node, with linkage from previous node
                previous_node, rel = self.graph_db.create({"type": "word", "name": word, "points": p},
                                                          (previous_node, "NEXTWORD", 0, {"points": p}))
            else:
                previous_node, = self.graph_db.create({"type": "word", "name": word, "points": p})

    def print_counts(self):
        for word in self.words:
            print "{0} - {1}".format(word, self.words[name])

    #steps is an array of the different rounds of analysis to be performed.
    #each one will analyzes the phrase with a different technique.
    #points from each step are weighted and normalized -todo
    def analyze(self, steps):
        for step in steps:
            if step == 'homophone':
                homophone.analyze(self.graph_db)
            elif step == 'hyphenation':
                hyphenations.analyze(self.graph_db)
            elif step == 'pos':
                part_of_speech.analyze(self.graph_db)
            elif step == 'definition':
                definition_linkage.analyze(self.graph_db)


    #over all the nodes and edges in the graph, sum the point values
    def compute_score(self):
        points_query = neo4j.CypherQuery(self.graph_db, "MATCH (n)-[r]->() RETURN SUM(n.points), SUM(r.points)")
        node_points, edge_points = points_query.execute()[0]
        return node_points + edge_points


