'''class HotelRoomCalc(object):
    'Hotel room rate calculator'
    def __init__(self, rt, sales = 0.085, rm = 0.1):
        HotelRoomCalc default arguments:
           sales tax == 8.5% and room tax == 10%
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days = 1):
        'Calculate totlal; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

sfo = HotelRoomCalc(299)
print sfo.calcTotal()
print sfo.calcTotal(2)

sea = HotelRoomCalc(189, 0.086, 0.058)
print sea.calcTotal()
print sea.calcTotal(4)

wasWkDay = HotelRoomCalc(169, 0.045, 0.02)
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02)

print wasWkDay.calcTotal(5) + wasWkEnd.calcTotal(2)'''

'''class P1(object):
        def foo(self):
            print 'called P1-foo()'

class P2(object):
        def foo(self):
            print 'called P2-foo()'
        def bar(self):
            print 'called P2-bar()'

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print 'called C2-bar()'

class GC(C1, C2):
    pass

gc = GC()
gc.foo()
gc.bar()'''

'''class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
        "Value must be a float!"
        self.value = round(val, 2)

    def __str__(self):
        return '.2%f' %self.value

    __repr__ = __str__

rfm = RoundFloatManual(3.2323)
print rfm'''

'''class Time60(object):
	'Time60 - track hours and minutes'
	def __init__(self, hr, min):
		'Time60 constructor - takes hours and minutes'
		self.hr = hr
		self.min = min
	def __str__(self):
		'Time60 - string representation'
		return '%d:%d' %(self.hr, self.min)
	__repr__ = __str__
	def __add__(self, other):
		'Time60 - overloading the addition operator'
		return self.__class__(self.hr + other.hr, self.min + other.min)
	def __iadd__(self, other):
		'Time60 - overloading in-placing addition'
		self.hr += other.hr
		self.min += other.min
		return self'''

from random import choice

class Randseq(object):
    def __init__(self, seq):
        self.data = seq
    def __iter__(self):
        return self
    def __next__(self):
        return choice(self.data)

#This is only test for GitHub, I want to know, if I add this line, what will happen?




































































































