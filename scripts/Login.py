#coding:utf-8
#!/usr/bin/env python

limitTimes = 3
tryTimes = 0
lock_file = account_lock.txt
account_file = account.txt

while limitTimes > tryTimes:
    username = raw_input('Please input your name:')
    lock_file = file(lock_file,'r')
    for line in lock_file:
        if username in line:
            print '%s is lockd' % username
            break
        else:
    	match_flg = False
    
