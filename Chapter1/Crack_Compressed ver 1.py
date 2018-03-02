import argparse
import rarfile
import zipfile
import sys
import os
from itertools import product
from threading import Thread
import time
import Queue

CHARACTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*,.'

parser = argparse.ArgumentParser(description = 'CompressedCrack v1.0', epilog = 'Use -h for help')
parser.add_argument('-f', dest = 'file', help = 'The compressed file name', required = True)
parser.add_argument('-min', dest = 'min', type = int , default = 0, help = '<minLength>')
parser.add_argument('-max', dest = 'max', type = int , default = 100, help = '<maxLength>')
parser.add_argument('-r', dest = 'rule', default = None, help = 'Password\'s rule')

options = parser.parse_args(['-f', 'test.rar'])


class Check:
    def __init__(self):
        self.min = options.min
        self.max = options.max 
        self.rule = options.rule
        self.file = options.file
            
        #KIEM TRA RULE
        if self.rule == None:
            self.rule = CHARACTER       

        #KIEM TRA LENGTH HOP LE
        if (self.min > self.max):
            print "Length Error"
            parser.exit()

        # KIEM TRA TYPE FILE
        if self.CheckFileExist(self.file):
            self.getType(self.file)
        else:
            print "No such file or directory: ", self.file

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
    def __init__(self, min, max, rule, type, file):
        self.min = min
        self.max = max
        self.rule = rule
        self.type = type
        self.file = file
        self.FIND = False
        
        # Kiem tra co length
        if self.min == 0 and self.max != 100:
            self.Rule_Length = 2    #DUYET TU 1 -> max
        elif self.min != 0 and self.max == 100:
            self.Rule_Length = 1    #DUYET TU min -> inf
        elif self.min != 0 and self.max != 100:
            self.Rule_Length = 3    #DUYET TU min -> max
        else :
            self.Rule_Length = 0    #DUYET TU 1 nf
        # MO FILE COMPRESSED
        if (self.type == '.rar'):
            self.FileCrack = rarfile.RarFile(self.file)
        else:
            self.FileCrack = zipfile.ZipFile(self.file)

        self.CheckPass()
        self.End_Crack()

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
                length +=1

        else:
            self.start = time.clock()
            length = 1
            while self.FIND == False:
                self.Brute(length)
                length += 1
            
    def Brute(self, length):
        listPass = product(self.rule, repeat = length)
        print 'Cracking password has', length, 'characters'
        for Pass in listPass:
            tryPass = ''.join(Pass)
            if self.type == '.rar':
                tryPass = tryPass.encode()
            #print tryPass
            if self.FIND == False:
                t = Thread(target = self.extractFile, args = (tryPass, ))
                t.setDaemon(True)
                t.start()
            
    def extractFile(self, password, ):
        try:
            self.FileCrack.extractall(pwd = password)
            print ('Complete')
            print 'Password: ',password
            print 'Time: ', time.clock() - self.start, 's' 
            print 'Wait for finishing threads...'
             #TIM DC PASSWORD
            self.FIND = True
        except:
            pass

    def End_Crack(self):
        if self.FIND == False:
            print 'Password not in this rule'
            sys.exit(0)
            parser.exit()           


def main():
    check = Check()     #lay cac parameter tu -i
    rarfile.UNRAR_TOOL = 'UnRAR.exe'
    handler = Handler(check.min, check.max, check.rule, check.type, check.file)


if __name__ =='__main__':
    main()
