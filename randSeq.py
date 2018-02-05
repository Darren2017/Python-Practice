#!/uer/bin/env python
#-*-coding:utf-8-*-

from random import choice

class Randseq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self
    
    def next(self):
        return choice(self.data)
    

example = Randseq('da')

if example == 'd':
    print 'd'
if example == 'a':
    print 'a'