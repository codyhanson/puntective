
import homophone
    
class Puntective:

    def __init__(self, phrase):
        self.phrase = phrase
        self.words = {}
        self.points = []

    def parse(self):
        #split the phrase into words, and count them.
        for word in self.phrase.split():
            #todo, better way to do this?
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1 

    def print_counts(self):
        for word in self.words:
            print "{0} - {1}".format(word, self.words[word])

    def analyze(self, steps):
        for step in steps:
            if step == 'homophone':
                self.points.append(homophone.analyze(self.words))
            elif step == 'hyphenations':
                print 'Hyphenations'


    def compute_score(self):
        total = 0
        for point_value in self.points:
            total += point_value
        return total


