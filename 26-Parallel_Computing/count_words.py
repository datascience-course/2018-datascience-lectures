#!/usr/bin/env python3
from mrjob.job import MRJob
import re

class MRCountWords(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            word = re.sub("[^a-zA-Z]+", "", word)
            yield word.lower(), 1

    def reducer(self, word, occurences):
        yield word, sum(occurences)

if __name__ == '__main__':
    MRCountWords.run()
