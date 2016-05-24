#!/usr/bin/env python
import sys
limitTimes = 3
tryTimes = 0
account_file = 'account.txt'
lock_file = 'account_lock.txt'

while limitTimes > tryTimes: 
    username = raw_input("Please input your name:")
    lock_check = file(lock_file)
    for line in lock_check.readlines():
    	if username in line:
    	    sys.exit('%s is locked' % username)
    password = raw_input('Password:')
    f = file(account_file,'rb')
    match_flag = False
    
    for line in f.readlines():
        user,passwd = line.strip('\n').split()
        if username == user and password == passwd:
            print 'Match!', username
            match_flag = True 
    	    break
    f.close()
    if match_flag == False:
        print 'User unmatched!'
    	tryTimes += 1
    else:
        print "Welcom login OldBoy learning system!!"
	break
else:
    print 'Your account is locked!'
    f = file(lock_file,'ab')
    f.write(username)
    f.close()

