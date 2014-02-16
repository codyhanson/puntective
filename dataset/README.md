#Generating the databases from the input files
run `seedDatabase.py` in order to slurp up the input files into a relational database,
in order to feed it into the puntective program.

This will seed the test phrases and puns, as well as any backing data that we 
import into a RDBMS for aid in analysis.

First version of `seedDatabase.py` will use SQLite 3, but it could be rewritten 
to use any datastore that you want.


#Datasources
homophones: http://www.opundo.com/homophones.htm

Puns: punoftheday.com

Phrases: Cody Hanson just made some stuff up, or picked ones that he liked.
