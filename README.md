puntective
==========

An AI program that attempts to detect whether an english phrase is a "pun". 
Various heuristics add nodes and edges to a graph database to encode humor
information between different parts of the phrase under examination.

For easy visualization of your graph, I recommend [Graffeine](https://github.com/julianbrowne/graffeine).

##Setup

###Install python dependencies
```bash
pip install -r requirements.txt
```

###Install neo4j graph database
[neo4j](http://www.neo4j.org/) is required as the graph database. Follow directions for your system,
and have it running on the default port.

###Getting NLTK datasets

Fire up a python shell
```python
>>> import nltk
>>> nltk.download()
```
A gui will pop up and you can pick which datasources to install. Safe bet is to install all of it.

###seeding sqlite
Sqlite is used for a simple homophone database, make sure it is installed
and then run:
```bash
./dataset/seedDb.py
```

##Running
To run all examples in dataset:
```bash
./run.py
```

To start an interactive shell:
```bash
./run_interactive.py
