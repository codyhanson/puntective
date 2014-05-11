#!/usr/bin/env python
from Puntective import Puntective
import json
from numpy import mean, median, max, min

phrase_file = open("./dataset/phrases.json")
phrases = json.load(phrase_file)
pun_scores = []
non_pun_scores = []
for phrase in phrases["phrases"]:
    p = Puntective(phrase["text"])
    is_pun = phrase["pun"]
    p.parse()
    p.analyze(['pos']) #part of speech
    p.analyze(['homophone'])
    p.analyze(['hyphenation'])
    p.analyze(['definition'])
    points = p.compute_score()
    print "Phrase (Pun?: {2}):{1} points - {0} ".format(phrase["text"], points, phrase["pun"])
    if is_pun:
        pun_scores.append(points)
    else:
        non_pun_scores.append(points)


print "Pun average:{0}".format(mean(pun_scores))
print "Pun median:{0}".format(median(pun_scores))
print "Pun max:{0}".format(max(pun_scores))
print "Pun min:{0}".format(min(pun_scores))
print "Non-Pun average:{0}".format(mean(non_pun_scores))
print "Non-Pun median:{0}".format(median(non_pun_scores))
print "Non-Pun max:{0}".format(max(non_pun_scores))
print "Non-Pun min:{0}".format(min(non_pun_scores))
