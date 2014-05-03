from py2neo import neo4j
from nltk.corpus import wordnet as wn
from collections import defaultdict
import operator



#this routine will scan each word in the phrase, and if it has a hyphenation, attach that information in a node via the edge
#it will also attach both sides of the hypenation as new nodes
def analyze(graph_db):
    #get all word nodes from db
    word_nodes_query = neo4j.CypherQuery(graph_db, 'MATCH (n) WHERE n.type="word" RETURN (n)')
    word_nodes = word_nodes_query.execute()
    words = [node.values[0]['name'] for node in word_nodes.data]
    for i in range(0, len(words)):
        syns = wn.synsets(words[i])
        #to determine the part of speech, take the majority pos from all synsets
        pos_count = defaultdict(int)
        for s in syns:
            pos_count[s.pos] += 1
        if len(pos_count) is not 0:
            pos = max(pos_count.iteritems(), key=operator.itemgetter(1))[0]
            graph_db.create({"type": "partofspeech", "name": pos, "points": 0},
                (word_nodes.data[i][0], "POS", 0, {"points": 0}))
