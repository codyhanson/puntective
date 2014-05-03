from nltk.corpus import wordnet as wn
from py2neo import neo4j
import re

point_scale_factor = 1
base_points = 10


#words we want to ignore, and parts of speech
exclusion_list = ['the', 'a', 'an', 'is', 'and', 'or', 'of', 'v', 'n', 's', 'r']

#scan each node in the graph, and look up the wordnet definition.
#then for each word in the definition, see if the word is in the graph somewhere, and add the link
def analyze(graph_db):
    #get ALL NODES from db
    nodes_query = neo4j.CypherQuery(graph_db, 'MATCH (n) RETURN (n)')
    nodes = nodes_query.execute()
    node_vals = [node.values[0]['name'] for node in nodes.data]
    for i in range(0, len(node_vals)):
        #lookup definitions for this node
        #but not if it is in the esclusion list
        if node_vals[i] in exclusion_list:
            continue
        syns = wn.synsets(node_vals[i])
        for s in syns[:3]:
            d = s.definition
            graph_db.create({"type": "definition", "name": s.lemma_names[0], "definition": d, "points": 0},
                            (nodes.data[i][0], "DEFINITION", 0, {"points": 0}))
    #now all definitions have been added, can we find linkages between them?
    defs = neo4j.CypherQuery(graph_db, 'MATCH (n) where n.type="definition" RETURN (n)').execute()
    for i in range(0, len(node_vals)):
        #lookup definitions for this node
        #but not if it is in the esclusion list
        if node_vals[i] in exclusion_list:
            continue
        for d in defs:
            if def_contains_word(node_vals[i].lower(), d[0]['definition']):
                #make an edge between the word and the definition
                graph_db.create((nodes.data[i][0], "DEFINITIONLINK", d[0], {"points": 0}))


def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


#word and definition are strings
def def_contains_word(word, definition):
    if find_whole_word(word)(definition) is not None:
        return True
    else:
        return False


