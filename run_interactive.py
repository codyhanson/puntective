#!/usr/bin/env python
from Puntective import Puntective


import fileinput
#import cmd
import sys

"""
class PuntectiveCmd(cmd.Cmd):

    def emptyline(self):
        pass

"""

#pcmd = PuntectiveCmd()
#pcmd.cmdloop()


while 1:
    try:
        line = raw_input("Enter a phrase for analysis>")
        if line:
            p = Puntective(line)
            p.parse()
            p.analyze(['pos'])
            p.analyze(['homophone'])
            p.analyze(['hyphenation'])
            p.analyze(['definition'])
            points = p.compute_score()
            print "Phrase '{0}'. Puntective score of: {1} points".format(line, points)
    except EOFError:
        print "\nGood bye"
        break

