
from py2neo import neo4j
import sqlite3 as db

conn = db.connect("./dataset/puntective.db")
conn.text_factory = str

point_scale_factor = 1
base_points = 10


def analyze(graph_db):
    points = 0
    #get all word nodes from db
    word_nodes_query = neo4j.CypherQuery(graph_db, 'MATCH (n) WHERE n.type="word" RETURN n')
    word_nodes = word_nodes_query.execute()[0]
    words = [node.value for node in word_nodes]
    cursor = conn.cursor()
    for word in words:
        cursor.execute("SELECT sounds_like FROM homophones WHERE key_word=?", (word,))
        rows = cursor.fetchall()
        for homophone in rows:
            if homophone[0] in words:
                print "Found homophones {0} - {1} in phrase. adding homophone edge with points".format(word, homophone[0])
                points = base_points * point_scale_factor
                #now we need to add an edge between the two words that were homophones.
                for node in word_nodes:
                    if node.value == homophone[0]:
                        graph_db.create()
    return points



