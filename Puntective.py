
import Homophone
    
class Puntective:

    def __init__(self, phrase):
        self.phrase = phrase
        self.words = {}

    def parse(self):
        #split the phrase into words, and count them.
        for word in self.phrase.split():
            #todo, better way to do this?
            if word in self.words:
                self.words[word] = self.words[word] + 1 
            else:
                self.words[word] = 1 

    def printCounts(self):
        for word in self.words:
            print "{0} - {1}".format(word,self.words[word])


    def analyze(self, rounds):
        for round in rounds:
            if round == 'homophone':
                Homophone(self.words)
            elif round == 'hyphenations':
                print 'Hyphenations'

