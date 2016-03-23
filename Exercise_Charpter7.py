#userpw.py
'''db = {}

def newUser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db[name] = pwd

def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'Welcome back', name
    else:
        print 'login incorrect!'

def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again!'
            else:
                chosen = True

        if choice == 'q':done = True
        if choice == 'n':newUser()
        if choice == 'e':olduser()

if __name__ == '__main__':
    showmenu()
'''
#7-5
'''import time
import datetime
db_pwd = {}
db_time = {}
db = {}
def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db_pwd.has_key(name):
            prompt = 'name taken, try again!'
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db_pwd[name] = pwd
    db_time[name] = datetime.datetime.now()

def olduser():
    name = raw_input('login: ')
    pwd = raw_input('pass word: ')
    passwd = db_pwd.get(name)
    if passwd == pwd:
        if  (datetime.datetime.now()- db_time[name]).seconds < 14400:
            print 'It"s too fast to login! '
        else:
            print 'Welcome back!', name
    else:
        print 'login incorrect!'

def deleteuser():
    name = raw_input('login:')
    pwd = raw_input('pass word:')
    passwd = db_pwd.get(name)
    if passwd == pwd:
        name_delete = raw_input('Who will be out?')
        print 'The user [%s] has been out!' % name_delete
        del db_pwd[name_delete]
    else:
        print 'Incorrect Password, You don"t have the permission!'

def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (D)elete User
    (Q)uit
    Enter choice:"""
    done = False
    while not done:
        chosen = False
        while not chosen:
           try:
                choice = raw_input(prompt).strip()[0].lower()
           except (EOFError, KeyboardInterrupt):
               choice = 'q'
               print '\nYou picked:[%s]' % choice
               if choice not in 'nedq':
                   print 'Invalid Option, try again!'
               else:
                   chosen = True
           if choice == 'q': done = True
           if choice == 'n': newuser()
           if choice == 'd': deleteuser()
           if choice == 'e': olduser()

if __name__ == '__main__':
    showmenu()
'''

#7-7
db_list = {}
db_num = {}
num_user = 0
def newUser():
    prompt = 'Login desired:'
    global num_user
    while True:
        name = raw_input(prompt)
        if db_list.has_key(name):
            prompt = 'name taken, try another!'
            continue
        else:
            num_user = num_user + 1
            break

    pwd = raw_input('passwd:')
    db_list[name] = pwd
    db_num[name] = num_user

def viewUser_name():
    print  'The user listed by name!'
    for key in sorted(db_list):
        print 'The user [%s] with the number: [%s]' % (key, db_num[key])
    else:
        print 'This company is too poor to hold anyone!'

def viewUser_num():
    print 'The user listed by number!'
    num_list = {}
    for key in db_num:
        num_list[db_num[key]] = key

    for key in sorted(num_list):
        print 'The number[%s] is [%s]' % (key, num_list[key])
    else:
        print 'This company is too poor to hold anyone!'

def showmenu():
    prompt = """
           (A)dd new User
           (V)iew Users
           (L)ist Users
           (Q)uit
           Enter choice:"""
    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYour picked: [%s]' % choice
            if choice not in 'avlq':
                print 'invalid option, try again!'
            else:
                choosen = True

            if choice == 'q':done = True
            if choice == 'a':newUser()
            if choice == 'v':viewUser_name()
            if choice == 'l':viewUser_num()

if __name__ == '__main__':
    showmenu()














































