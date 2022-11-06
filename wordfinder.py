"""Word Finder: finds random words from a dictionary."""
# import Math
import random

class WordFinder:
    ...

    def __init__(self, file):
        self.file = file
        self.count = 0

    def __repr__(self):
        file = open(self.file, 'r')
        # print(file.read())
        for line in file:
            # print(line)
            self.count = self.count + 1
            # print(self.count)
        file.close()
        print(self.count)
        return self.count

    def random(self):
        '''Chooses a random word from the text file'''
        words = []
        file = open(self.file, 'r')
        for line in file:
            sw = line.strip()
            # print(sw)
            words.append(sw)
        # print(words)
        # print(len(words))
        file.close()
        rnum = random.randint(0, len(words))
        print (words[rnum])
        return words[rnum]

class SpecialWordFinder(WordFinder):
    '''Finds special words without headings'''

    def __init__(self, file):
        super().__init__(file)


    def chooseRandomSpecialWord(self):
        words = []
        file = open(self.file, 'r')
        for line in file:
            sw = line.strip()
            # print(sw)
            # print(len(sw))
            if len(sw) == 0 or sw[0] == '#':
                print("")
            else:
                # print(sw)

                words.append(sw)
        
        file.close()
        # print(words)
        # print(len(words))
        rnum = random.randint(0, len(words) - 1)
        print(words[rnum])
        return words[rnum]


swf = SpecialWordFinder('spwords.txt').chooseRandomSpecialWord()
# wf = WordFinder(('words.txt')).random()
# print(random.randint(0, ))