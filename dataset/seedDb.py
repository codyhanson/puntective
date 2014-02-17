
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

"""
#Wow this was a really bad way to do this.

print "Creating the thesaurus table"

cursor.execute("CREATE TABLE thesaurus(key_word TEXT, synonym TEXT)")

print "populating the thesaurus table"

thes_file = "thesaurus/mobythes.csv"
thes_hdl = open(thes_file, 'r')

#this nesting is ugly, but hey, its research code.
for line in thes_hdl:
    words = line.split(',')
    print "{0} synonyms in this entry".format(len(words))
    thes_to_insert = []
    for key_word in words:
        for synonym in words:
            #don't make associations with the same word
            if key_word != synonym:
                thes_to_insert.append((key_word.rstrip(),synonym.rstrip()))
    print "Inserting {0} records into thesaurus table".format(len(thes_to_insert))
    cursor.executemany("INSERT INTO thesaurus VALUES(?,?)", tuple(thes_to_insert))
"""















#Make it so
conn.commit()
