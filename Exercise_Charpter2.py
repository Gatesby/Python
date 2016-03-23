'''count = 0
while count < 3:
    print 'loop #%d' % (count)
    count += 1
'''

'''print 'I like to use the Internet for:'
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item,
print
'''

'''who = 'knights'
what = 'Ni!'
print 'We are the', who, 'who say', what, what, what, what
print 'We are the %s who say %s' % \
      (who, (what + ' ') * 4)
'''

#2-4 practice_of_raw_input()
'''str1 = raw_input('Please Enter a favorite characters:')
print 'Your favorite character is:', str1

str2 = raw_input('Please input your lucky number:')
print 'Doubling your number: %d' % (int(str2))
'''

#2-5 pratice_of_while
'''index = 0
while index < 11:
    print index,
    index += 1
print

index2 = 0
for index2 in range(11):
    print index2,
print
'''

'''#2-6 To judge a number whether negative or positive
num = int(raw_input('Please input a number to judge positive or not:'))
if num > 0:
    print 'This Number is positive'
elif num < 0:
    print 'This Number is Negative'
else:
    print 'This Number is Zero'
'''

'''#2-7 pratice_of_loop&string
str1 = raw_input('Please input a string:')
num = 0
len_str1 = len(str1)
while num < len_str1:
    print str1[num],
    num += 1
print
'''
#2-8-1 practice_of_while
'''index = 0
sum = 0
while index < 5:
    num = int(raw_input('Please input a number:'))
    print 'The number you input is:', num
    sum += num
    index += 1
print 'The summer of five numbers is:', sum
'''

#2-8-2 practice_of_for
'''sum = 0
for eachNum in range(5):
    eachNum = int(raw_input('Please Enter a number:'))
    sum += eachNum
print 'The sum of five numbers is:', sum
'''

#2-9 practice_of_float
'''average = 0
sum = 0
for eachNum in range(5):
    sum += float(raw_input('Please Enter a number:'))
average = sum / 5
print 'The average of five number is:', average
'''

#2-15
'''print 'Enter three numbers:'
num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())
min = num1
if min > num2:
    min = num2
    if min > num3:
        print num3, num2, num1
    elif num1 > num3:
        print num2, num3, num1
    else
        print num2, num1, num3
elif min > num3:
    print num3,num1,num2
elif num3 > num2:
    print num1,num2,num3
else:
    print num1,num3,num2
    '''