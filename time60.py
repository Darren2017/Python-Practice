#!/uer/bin/env python
#-*-coding:utf-8-*-

class Time60(object):
    'Time60 - track hours and minutes'
    
    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - srting repersentation'
        return '%02d:%02d' % (self.hr, self.min)

    __repr__ = __str__
    
    def __add__(self, other):

        'Time60 - overloading the addition operator'
        if self.min + other.min > 60:
            return self.__class__(self.hr + other.hr + 1, self.min + other.min -60)
        else:
            return self.__class__(self.hr + other.hr, self.min + other.min)
    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        if self.min + other.min > 60:
            self.hr += (other.hr + 1)
            self.min += (other.min - 60)
        else:
            self.hr += other.hr
            self.min += other.min
        return self

mon = Time60(10, 30)
tue = Time60(11, 55)

print tue

print id(mon)

mon += tue

print id(mon)

print mon
