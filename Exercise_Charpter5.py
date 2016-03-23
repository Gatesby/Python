#5-2
'''def Sum_Two_Num(num1, num2):
    print 'The sum of', num1, 'and', num2, 'is', num1+num2

Sum_Two_Num(2,3)'''

#5-3
'''import types
def The_Grade_Of_Student(score):
    if isinstance(score,int):
        if 90 <= score < 100:
            print 'The score of student is:A!'
        elif 80 <= score < 89:
            print 'The score of student is B!'
        elif 70 <= score < 79:
            print 'The score of student is C!'
        elif 60 <= score < 69:
            print 'The score of student is D!'
        elif 0 <= score < 59:
            print 'The score of student is F!'
        else:
            print 'Please input the correct score!'
    else:
        print 'Please input the correct score!'

The_Grade_Of_Student(80)'''

#5-4
'''def cal_leap_year():
    try:
        year = int(raw_input("Please input a year:"))
        if year % 4 == 0 and year % 100 != 0:
            print '%d is a leap year' %year
        elif year % 400 == 0:
            print '%d is a leap year' %year
        else:
            print '%d is not a leap year' %year
    except ValueError, e:
        print 'you must input a digit'
cal_leap_year()'''

#5-5
'''try:
    dollar = float(raw_input('Input the money that less than 1 dollar:'))
    if dollar >= 1:
        print 'money is too large.'
    elif 0 < dollar < 1:
        temp = int(dollar * 100)
        (N25, temp) = divmod(temp, 25)
        print "%d 25 coins." %N25
        (N10, temp) = divmod(temp, 10)
        print "%d 10 coins." %N10
        (N5, temp) = divmod(temp, 5)
        print "%d 5 coins." %N5
        (N1,temp) = divmod(temp, 1)
        print "%d 1 coins" %N1
    else:
        print "You must input larger tha 0."
except ValueError, e:
    print "You must input a digit"
'''
#5-6
'''print 'Enter the expression:'
expression = raw_input('>')

if len(expression.split('+')) == 2:
    try:
        splitExpression = expression.split('+')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m + n
    except ValueError, e:
        print "Input ValueError!"
elif len(expression.split('-')) == 2:
    try:
        splitExpression = expression.split('-')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m - n
    except ValueError, e:
        print "Input ValueError !"
elif len(expression.split('*')) == 2:
    try:
        splitExpression = expression.split('*')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m * n
    except ValueError, e:
        print "Input ValueError !"
elif len(expression.split('/')) == 2:
    try:
        splitExpression = expression.split('/')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m / n
    except ValueError, e:
        print 'Input ValueError !'
elif len(expression.split('%')) == 2:
    try:
        splitExpression = expression.split('%')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m % n
    except ValueError, e:
        print 'Input ValueError!'
elif len(expression.split('**')) == 2:
    try:
        splitExpression = expression.split('**')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
    except ValueError, e:
        print 'Input ValueError !'
else:
        print 'Input Error'
'''

'''#5-8
from math import pi

def square(length):
    area = length ** 2
    print 'The area of square is %0.2f' %area

def cube(length):
    volume = length ** 3
    print 'The volume of cube is %0.2f' %volume

def circle(radius):
    area = pi * radius ** 2
    print 'The area of circle is %0.2f' %area

def sphere(radius):
    volume = 4 * pi * radius ** 2
    print 'The volume of sphere is %0.2f' %volume
if __name__ == "__main__":
    try:
        print '******Direct execute******'
        num = float(raw_input("Enter a num:"))
        square(num)
        cube(num)
        circle(num)
        sphere(num)
    except ValueError, e:
        print 'Input a invaild num!'
if __name__ == 'test':
    try:
        print "******Module called******"
        num = float(raw_input("Enter a num:"))
        square(num)
        cube(num)
        circle(num)
        sphere(num)
    except ValueError, e:
        print "Input a invaild num!"
'''

