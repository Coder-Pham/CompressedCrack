import argparse
import rarfile
import zipfile
import sys
import os
from itertools import product
import threading
import time
import Queue

exitflag = 0
CHARACTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*,.'

parser = argparse.ArgumentParser(description = 'CompressedCrack v1.0', epilog = 'Use -h for help')
parser.add_argument('-f', dest='file', help='The compressed file name', required=True)
parser.add_argument('-min', dest='min', type=int, default=0, help='<minLength>')
parser.add_argument('-max', dest='max', type=int, default=100, help='<maxLength>')
parser.add_argument('-r', dest='rule', default=None, help='Password\'s rule')

options = parser.parse_args()

'''
class myThread(threading.Thread):
    def __int__(self, FileCrack, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.FileCrack = FileCrack
'''


class myThread(threading.Thread):
    def __init__(self, FileCrack, name, q):
        threading.Thread.__init__(self)
        self.FileCrack = FileCrack
        self.name = name
        self.q = q

    def run(self):
        extractFile(self.FileCrack, self.q)


def extractFile(FileCrack, q):
    """
    It processes items in a queue 1 after another.
    These daemon threads go into infinite loop, will end when
    main thread end.
    """
    global exitflag
    while not exitflag:
        queueLock.acquire()
        if not workQueue.empty():
            password = q.get()      #block here until it have sth do to
            queueLock.release()
            try:
                FileCrack.extractall(pwd=password)
                print ('Complete')
                print 'Password: ', password
                # print 'Time: ', time.clock() - self.start, 's'
                print 'Wait for finishing threads...'

                # TIM DC PASSWORD
                handler.FIND = True
                workQueue.queue.clear()     # Clear all exist password in queue
            except:
                pass
        else:
            queueLock.release()


class Check:
    def __init__(self):
        self.min = options.min
        self.max = options.max 
        self.rule = options.rule
        self.file = options.file
            
        #KIEM TRA RULE
        if self.rule==None:
            self.rule = CHARACTER       

        #KIEM TRA LENGTH HOP LE
        if (self.min > self.max):
            print "Length Error"
            parser.exit()

        #KIEM TRA TYPE FILE
        if self.CheckFileExist(self.file):
            self.getType(self.file)
        else:
            print "No such file or directory: ", self.file

        # MO FILE COMPRESSED
        if self.type == '.rar':
            self.FileCrack = rarfile.RarFile(self.file)
        else:
            self.FileCrack = zipfile.ZipFile(self.file)

    def CheckFileExist(self, file):
        if os.path.isfile(file):
            return True
        else:
            return False

    def getType(self, file):
        if (os.path.splitext(file)[1] == '.rar' or os.path.splitext(file)[1] == '.zip'):
            self.type = os.path.splitext(file)[1]
        else:
            print 'Extension Error'
            parser.exit()


class Handler:
    def __init__(self, min, max, rule, type, FileCrack):
        self.min = min
        self.max = max
        self.rule = rule
        self.type = type
        self.FileCrack = FileCrack
        self.FIND = False
        
        # Kiem tra co length
        if self.min == 0 and self.max != 100:
            self.Rule_Length = 2    # DUYET TU 1 -> max
        elif self.min != 0 and self.max == 100:
            self.Rule_Length = 1    # DUYET TU min -> inf
        elif self.min != 0 and self.max != 100:
            self.Rule_Length = 3    # DUYET TU min -> max
        else :
            self.Rule_Length = 0    # DUYET TU 1 nf

        self.CheckPass()

    def CheckPass(self):
        if self.Rule_Length == 3:
            self.start = time.clock()
            for length in range(self.min, self.max + 1):
                if self.FIND == False:
                    self.Brute(length)

        elif self.Rule_Length == 2:
            self.start = time.clock()
            for length in range(1, self.max + 1):
                if self.FIND == False:
                    self.Brute(length)

        elif self.Rule_Length == 1:
            self.start = time.clock()
            length = self.min
            while self.FIND == False:
                self.Brute(length)
                length += 1

        else:
            self.start = time.clock()
            length = 1
            while self.FIND == False:
                self.Brute(length)
                length += 1
            
    def Brute(self, length):
        listPass = product(self.rule, repeat=length)

        # Fill the queue
        queueLock.acquire()

        print 'Cracking password has', length, 'characters'
        for Pass in listPass:
            tryPass = ''.join(Pass)
            if self.type == '.rar':
                tryPass = tryPass.encode()
            workQueue.put(tryPass)
        queueLock.release()

        '''
        Using queue for threading from this line
        Threads created from new class with 2 def function
        1/ __init__ 
        2/ run
        The run function is the extractFile function in Handler
        '''

        # Wait for empty queue
        while not workQueue.empty():
            pass

        # Wait for finish all threads
        for t in threads:
            t.join()

    '''
    def End_Crack(self):
        if self.FIND == False:
            print 'Password not in this rule'
            sys.exit(0)
            parser.exit()           
    '''


# Number of threads used in process
threadList = ["Thread-1", "Thread-2", "Thread-3"]
queueLock = threading.Lock()
workQueue = Queue.Queue(-1)  # Unlimited storage for queue with -1
threads = []


check = Check()   
rarfile.UNRAR_TOOL = 'UnRAR.exe'

# Create new threads
for tName in threadList:
    thread = myThread(check.FileCrack, tName, workQueue)
    thread.start()
    threads.append(thread)

handler = Handler(check.min, check.max, check.rule, check.type, check.FileCrack)
