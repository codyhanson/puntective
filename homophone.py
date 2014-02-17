
import sqlite3 as db

conn = db.connect("./dataset/puntective.db")
conn.text_factory = str

point_scale_factor = 1
base_points = 10


def analyze(word_counts):
    points = 0
    cursor = conn.cursor()
    for key in word_counts.keys():
        cursor.execute("SELECT sounds_like FROM homophones WHERE key_word=?", (key,))
        rows = cursor.fetchall()
        for homophone in rows:
            if homophone[0] in word_counts:
                print "Found homophones {0} - {1} in phrase. adding points".format(key, homophone[0])
                points += base_points * point_scale_factor + word_counts[homophone[0]]
    return points



