from pymorphy2 import MorphAnalyzer
import os
import random
import argparse
import sys

class AnecdoteManager:

    def __init__(self, folder='anecdotes'):

        self._load_anec_files('/'.join([sys.path[0], folder]))
    
    def _normal_form(self, phrase):
        
        morph = MorphAnalyzer()
        
        words = phrase.split()
        normal_words = []
        for word in words:
            normal_words.append(morph.parse(word)[0].normal_form)

        return ' '.join(normal_words)


    def _load_anec_files(self, folder):

        self.lfiles = os.listdir(folder)
        self.files = []
        self.nf_files = dict()
        for file in self.lfiles:
            ffile = '/'.join([folder, file])
            self.files.append(ffile)
            self.nf_files[self._normal_form(file)] = ffile


    def get_anecdote(self, theme):
        try:
            if theme == 'any':
                theme = self.lfiles[random.randint(0, len(self.lfiles) - 1)]
            afile = open(self.nf_files[self._normal_form(theme)], 'r')
            anecdotes = afile.readlines()
            afile.close()
            return anecdotes[random.randint(0, len(anecdotes) - 1)].split('<li>')[1].split('</li>')[0]
        except KeyError:
            return "Не знаю анекдоты про " + theme



def main(theme):

    am = AnecdoteManager()
    print(am.get_anecdote(theme))
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--theme', default='any')
    args = parser.parse_args()

    main(theme=args.theme.strip())
    
