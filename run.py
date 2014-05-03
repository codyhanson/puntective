#!/usr/bin/env python
from Puntective import Puntective
import json

phrase_file = open("./dataset/phrases.json")
phrases = json.load(phrase_file)

for phrase in phrases["phrases"]:
    p = Puntective(phrase["text"])
    p.parse()
    p.analyze(['pos']) #part of speech
    p.analyze(['homophone'])
    p.analyze(['hyphenation'])
    p.analyze(['definition'])
    points = p.compute_score()
    print "Phrase (Pun?: {2}): {0} got {1} points".format(phrase["text"], points, phrase["pun"])
