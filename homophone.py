
from py2neo import neo4j
import sqlite3 as db

conn = db.connect("./dataset/puntective.db")
conn.text_factory = str

point_scale_factor = 1
base_points = 10

#this routine will scan each word in the phrase, and if it has a homophone, attach it via an edge.
def analyze(graph_db):
    points = 0
    #get all word nodes from db
    word_nodes_query = neo4j.CypherQuery(graph_db, 'MATCH (n) WHERE n.type="word" RETURN (n)')
    word_nodes = word_nodes_query.execute()
    words = [node.values[0]['name'] for node in word_nodes.data]
    cursor = conn.cursor()
    for i in range(0,len(words)):
        cursor.execute("SELECT sounds_like FROM homophones WHERE key_word=?", (words[i],))
        rows = cursor.fetchall()
        for homophone in rows:
            graph_db.create({"type":"homophone", "name":homophone[0], "points":base_points},
                            (word_nodes.data[i][0], "HOMOPHONE", 0, {"points":base_points}))



