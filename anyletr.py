#!/usr/bin/env python
#-*-coding:utf-8-*-

class AnyIter(object):
    def __init__(self, data, safe = False):
        self.safe = safe
        self.iter = iter(data)

    def ___iter__(self):
        return self

    def next(self, howmany = 1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                     break
                else:
                    raise
        return retval

a = AnyIter(range(160), True)
for j in range(14):
    print j, ':', a.next(j)
