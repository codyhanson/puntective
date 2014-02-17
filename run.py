from Puntective import Puntective

p = Puntective('a b c d d a')
p.parse()
p.printCounts()
p.analyze(['homophone'])
