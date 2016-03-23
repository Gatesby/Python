'''import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker V1.0'
print 'Testees must be at least 2 chars long'
myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print invaild: first symobl must be
                alphabetic
    else:
            for otherChar in myInput[1:]:

                if otherChar not in alphas+nums:
                    print invalid: remaining
                          symbols must be alphanumeric
                    break
            else:
              print "okay as an identifier"
'''


'''#stack.py

stack = []

def pushit():
    stack.append(raw_input('Enter New string: ').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [', `stack.pop()`, ']'

def viewstack():
    print stack

CMDs = {'u':pushit, 'o':popit, 'v':viewstack}

def showmenu():
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit

    Enter coice:"""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option, try again!'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
'''

'''#queue.py

queue = []

def enQ():
    queue.append(raw_input('Enter New String: ').strip())

def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue!'
    else:
        print 'Removed[', `queue.pop(0)`, ']'

def viewQ():
    print queue #calls str() internally

CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}

def showMenu():
    pr = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit
Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'devq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showMenu()'''

'''#6-2

import string


alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

iden = raw_input('Identifier to check? ')

if len(iden) > 0:
    if iden(0) not in alphas:
        print "Error: First char must be alphabetc"
    else:
        if len(iden) > 1:
            for eachChar in iden[1:]:
                if eachChar not in alnums:
                    print "Error: others must be alnum"
                    break
            else:
                import keyword
                if iden not in keyword.kwlist:
                    print 'Ok'
                else:
                    print 'Error: keyword name'
else:
    print 'Error: no identifier entered'
'''
'''#6-3
def get_num():
    global num_list
    num_list = []
    num = ''
    while num != '!':
        num = raw_input('a').strip()
        if num != '!':
            try:
                num = float(num)
            except:
                print 'Error,Again!'
                get_num()
            else:
                num_list.append(num)
        else:
            break
    return num_list
def sort_descending():
    get_num()
    print sorted(num_list, reverse = True)

print '------------------------(a)----------------------'
sort_descending()

print '------------------------(b)----------------------'
key_sort = []
while True:
    k = raw_input('b')
    if k != '#':
        key_sort.append(k)
    else:
        break
print sorted(key_sort, reverse = True)
'''
'''#6-4
scoreList = []
while True:
    try:
        score = float(raw_input('Please input scores:...'))
        scoreList.append(score)
    except:
        print 'You did not input a correct score.Program stopped'
        break
print scoreList
i = 0
for k in scoreList:
    i = i + k
print 'The average is %4.2f' %(i / len(scoreList))
'''

'''#6-6
def blank():
    get_str = raw_input('Please in put your string:')
    r = len(get_str) - 1
    l = 0
    while get_str[l] == ' ':
        l = l + 1
    while get_str[r] == ' ':
        r = r - 1
    result = get_str[l:r + 1]
    return result

if __name__ == '__main__':
    print blank()
'''
'''#6-7

num_str = raw_input('Enter a number:')

num_num = int(num_str)

fac_list = range(1,num_num + 1)
print "BEFORE", `fac_list`

i = 0
while i < len(fac_list):

    if num_num % fac_list[i] == 0:
        del fac_list[i]
        continue
    i = i + 1
print "AFTER:", `fac_list`
'''
# 6-8
'''def get():
    global get_num
    get_num = raw_input('Please input your number:')
    try:
        get_num = int(get_num)
    except:
        print 'Error Input,please input a number!'
        get()
    else:
        print 'Input success!'

eng_list = []
eng = "zero, one, two, three, four, five, six, seven, eight, nine, ten"
eng_list = eng.split(',')
result = []
get()
get_list = list(str(get_num))
for i in get_list:
    result.append(eng_list[int(i)])
print '-'.join(result)
print '-------------------------'
str_1 = "zero, one, two, three, four, five, six, seven, eight, nine"
str_2 = "ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty"
str_3 = "thirty, forty, fifty, sixty, seventy, eighty, ninety"
eng_1 = []
eng_2 = []
eng_3 = []
eng_1 = str_1.split(',')
eng_2 = str_2.split(',')
eng_3 = str_3.split(',')

get()

kilo = get_num / 1000
hund = get_num % 1000 / 100
deca = get_num % 1000 % 100 / 10
unit = get_num % 1000 % 100 % 10

if kilo != 0:
    if hund != 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred'
    elif hund == 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(kilo)],'thousand','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(kilo)],'thousand','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(kilo)],'thousand',
elif kilo == 0:
    if hund != 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(hund)],'hundred','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(hund)],'hundred','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(hund)],'hundred'
    elif hund == 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_2[int(unit)]
        elif int(deca)==0:
            print eng_1[int(unit)]
'''

#6-9
'''def m_trans_h():
    get_time = int(raw_input('Please input your time:'))
    hour = get_time / 60
    minute = get_time % 60
    print hour, 'H', ':', minute, 'M'
'''

#6-10
'''str_1 = raw_input("Enter your string:")
str_list = list(str_1)
result_list = []
for i in str_list:
    if i.isupper():
        result_list.append(i.lower())
    elif i.islower():
        result_list.append(i.upper())
    else:
        result_list.append(i)
result = ''.join(result_list)
print 'Before:%s' % str_1
print 'After:%s' % result
'''

#6-12
import types
def findchr(string, char):
    print 'The string is "%s" and the char is "%s"' % (string, char)
    result = []
    for i,j in enumerate(string):
        if char == j:
            result.append(i)
    if len(result) != 0:
        print 'The index of char:'
        return result
    else:
        return -1

def rfindchr(string, char):
    print 'The string is "%s" and the char is "%s"' % (string, char)
    l = len(string)
    for i,j in enumerate(string[::-1]):
        if char == j:
            result = l - i
            break
































































