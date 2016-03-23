'''from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MATRIES = 2

def doprob():
    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse = True)
    ans = ops[op](*nums)
    pr = '%d %s %d =' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'Correct!'
                break
            if oops == MATRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again!'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
                print 'invalid input..., try again!'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
                break

if __name__ == '__main__':
    main()'''

'''from time import ctime, sleep
def tsfunc(func):
	def wrappedFunc():
		print '[%s] %s() called' % (ctime(), func.__name__)
		return func()
	return wrappedFunc

@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()'''

'''def convert(func, seq):
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 9999999L)

print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)'''

'''from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.stirp():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines),
    lines.reverse()
    print firstNonBlank(lines),

def download(url = 'http://www', process = firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    download()'''

'''def tupleVarArgs(arg1, arg2 = 'defaultB', *theRest) :
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg

tupleVarArgs('abc', 123, 'xyz', 456.780)'''


'''def dictVarArgs(arg1, arg2 = 'defaultB', **theRest) :
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg]))'''

#dictVarArgs('one', d = 10, e = 'zoo', men = ('freud', 'gaudi'))

'''def newfoo(arg1, arg2, *nkw, **kw):
    print 'arg1 is: ', arg1
    print 'arg2 is: ', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg: ', eachNKW
    for eachKW in kw:
        print "additional keyword arg '%s': %s" % (eachKW, kw[eachKW])'''

#newfoo(2, 4, *(6, 8), **{'foo': 10, 'bar':12})

'''def testit(func, *nkwargs, **kwargs):
    try:
        revtal = func(*nkwargs, **kwargs)
        result = (True, revtal)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0] :
                print '%s(%s) = ' % (eachFunc.__name__, eachVal), retval[1]
            else:
                print '%s(%s) = FAILED:' % (eachFunc.__name__, eachVal), retval[1]


if __name__ == '__main__':
    test()'''

'''from random import randint
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(lambda n : n % 2, allNums)

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print [n for n in allNums if n % 2]

allNums = []
from random import randint as ri
print [n for n in [ri(1, 99) for i in range(9)] if n % 2]
'''
#map((lambda x: x + 2), [0, 1, 2, 3, 4, 5 ])

'''from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg = 'white', bg = 'blue')
b1 = MyButton(text = 'Button1')
b2 = MyButton(text = 'Button2')
qb = MyButton(text = 'QUIT', bg = 'red', command = root.quit)
b1.pack()
b2.pack()
qb.pack(fill = Tkinter.X, expand = True)
root.title('PFAs')
root.mainloop()'''

'''output = '<int %r id = %#0x val = %d'
w = x = y = z = 1

def f1():
    x = y = z = 2

def f2():
    y = z = 3
    def f3():
        z = 4
        print output % ('w', id(w), w)
        print output % ('x', id(x), x)
        print output % ('y', id(y), y)
        print output % ('z', id(z), z)

    clo = f3.func_closure
    if clo:
        print "f3 closure vars:", [str(c) for c in clo]
    else:
        print "no f3 closure vars"

    f3()

    clo = f2.func_closure
    if clo:
        print "f2 closure vars:", [str(c) for c in clo]
    else:
        print "no f2 closure vars"
    f2()

clo = f1.func_closure
if clo:
    print "f1 closure vars:", [str(c) for c in clo]
else:
    print "no f1 closure vars"

f1()'''

'''from time import time

def logged(when):
    def log(f, *args, **kargs):
        print Called:
        function: %s
        args: %r
        kargs: %r %(f, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapped(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "time delta: %s" % (time() - now)
        return wrapped

    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@logged("post")
def hello(name):
    print "Hello,", name

hello("World!")'''

'''from random import randint
def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList)))

for item in randGen(['rock', 'paper', 'scissors']):
    print item'''

#11-3 the restructure of max and min
'''from functools import partial
def max2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return  num2

def min2(num1, num2):
    if num1 < num2 :
        return num1
    else :
        return num2


def main():
    print 'Please input two numbers:'
    while True:
        try:
             num1 = raw_input('The first number is:')
             num2 = raw_input('The second number is:')

             if num1.isdigit() and num2.isdigit():
                 print "the Bigger number of ", num1," and", num2, " is ", max2(num1, num2)
                 break
             else:
                 print "Please input numbers!"
        except Exception, dialog:
             retval = str(dialog)
             print "There are a problem here:", retval

list_number = [1, 2, 3, 4, 5, 6]
max_strength = reduce(max2, list_number)
min_strength = reduce(min2, list_number)
print "The maximum of one list is", max_strength, " and ", "The minimum of one list is", min_strength'''
#11-7
'''list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]
print map(None, list1, list2),'\n', zip(list1, list2)'''
#11-8
'''def cal_leap_year(year):
    try:
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    except ValueError, e:
        print 'you must input a digit'

year_determine = [1002, 1003, 1004, 2000, 2005, 2004, 2008, 2016, 2012]
#year_leap = filter(cal_leap_year, year_determine)
print [year for year in year_determine if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]'''

#11-9
'''The_number_to_sum = [1, 2, 3, 4, 5, 6, 7]
print 'The average of these number is:', float(reduce((lambda x, y: x + y), The_number_to_sum)) / len(The_number_to_sum)
'''











































































































































































































