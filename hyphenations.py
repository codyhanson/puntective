from py2neo import neo4j
import re



point_scale_factor = 1
base_points = 2

hyphen_pattern = re.compile('(.+?)-(.+)')

#this routine will scan each word in the phrase, and if it has a hyphenation, attach that information in a node via the edge
#it will also attach both sides of the hypenation as new nodes
def analyze(graph_db):
    #get all word nodes from db
    word_nodes_query = neo4j.CypherQuery(graph_db, 'MATCH (n) WHERE n.type="word" RETURN (n)')
    word_nodes = word_nodes_query.execute()
    words = [node.values[0]['name'] for node in word_nodes.data]
    for i in range(0,len(words)):
        m = re.match(hyphen_pattern, words[i])
        if m is not None:
            first = m.group(1)
            second = m.group(2)
            #add first node
            graph_db.create({"type":"hyphenation", "name":first, "points":base_points},
                            (word_nodes.data[i][0], "HYPHEN", 0, {"points":base_points}))
            #add second node
            graph_db.create({"type":"hyphenation", "name":second, "points":base_points},
                            (word_nodes.data[i][0], "HYPHEN", 0, {"points":base_points}))

