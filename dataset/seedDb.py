
import sqlite3 as db
import os

db_name = "puntective.db"

print "Removing {0}".format(db_name)
## if file exists, delete it ##
if os.path.isfile(db_name):
    os.remove(db_name)

#Connect to brand new database
conn = db.connect(db_name)
conn.text_factory = str

cursor = conn.cursor()


print "Creating the homophones table"

cursor.execute("CREATE TABLE homophones(key_word TEXT, sounds_like TEXT)")

print "populating the homophones table"

homophones_file = "homophones.csv"
homophones_to_insert = []
homophones_hdl = open(homophones_file, 'r')

#this nesting is ugly, but hey, its research code.
for line in homophones_hdl:
    words = line.split(',')
    for keyword in words:
        for sounds_like in words:
            #don't make associations with the same word
            if keyword != sounds_like:
                homophones_to_insert.append((keyword.rstrip(),sounds_like.rstrip()))

cursor.executemany("INSERT INTO homophones VALUES(?,?)", tuple(homophones_to_insert))

#Make it so
conn.commit()
