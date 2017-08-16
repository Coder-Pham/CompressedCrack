import argparse
import zipfile
import sys
from itertools import product
from threading import Thread
import time

CHARACTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*,.'

parser = argparse.ArgumentParser(prog = 'CompressedCrack zipfile v1.0',epilog = 'Ex:Zip.py -i <filename>  <minLength>  <maxLength>  -r <Characters rules>')
parser.add_argument('-z', dest = 'zip', help = 'The zip file name', required = True)
parser.add_argument('-min', dest = 'min', type = int , default = 100, help = '<minLength>')
parser.add_argument('-max', dest = 'max', type = int , default = 100, help = '<maxLength>')
parser.add_argument('-r', dest = 'rule', default = None, help = 'Password\'s rule')

options = parser.parse_args()

class Check:
    def __init__(self):
        self.min = options.min 
        self.max = options.max 
        self.rule = options.rule
            
        #KIEM TRA RULE
        if self.rule == None:
            self.rule = CHARACTER       

        #KIEM TRA LENGTH HOP LE
        if (self.min > self.max) and (self.min != 100) and (self.max != 100):
            print "Length Error"
            parser.exit()

class Handler:
    def __init__(self, min, max, rule):
        self.min = min
        self.max = max
        self.rule = rule
        self.FIND = False
        
        #Kiem tra co length
        if self.min == 0 and self.max != 0:
            self.Rule_Length = 2    #DUYET TU 1 -> max
        elif self.min != 0 and self.max == 0: 
            self.Rule_Length = 1    #DUYET TU min -> inf
        elif self.min != 0 and self.max != 0:
            self.Rule_Length = 3
        else :
            self.Rule_Length = 0    #DUYET TU 1 -> inf
        #MO FILE ZIP
        self.open(options.zip)
        self.CheckPass()

    def open(self,FileName):
        self.zfile = zipfile.ZipFile(FileName)
                
        #DANH DAU TG BAT DAU
        self.start = time.clock()
        print 'Cracking...'
    
    def CheckPass(self):
        if self.Rule_Length == 3:
            for length in range(self.min, self.max + 1):
                if self.FIND == False:
                    self.Brute(length)
            self.End_Crack()

        elif self.Rule_Length == 2:
            for length in range(1, self.max + 1):
                if self.FIND == False:
                    self.Brute(length)

        elif self.Rule_Length == 1:
            length = self.min
            while self.FIND == False:
                self.Brute(length)
                length +=1
        else:
            length = 1
            while self.FIND == False:
                self.Brute(length)
                length+=1          
            
    def Brute(self, length):
        listPass = product(self.rule, repeat = length)
        print 'Cracking password has', length, 'characters'
        for Pass in listPass:
            tryPass = ''.join(Pass)
            tryPass = tryPass.encode()
            # print tryPass
            t = Thread(target = self.extractFile, args = (tryPass, ))
            t.start()
            
    def extractFile(self, password):
        try:
            self.zfile.extractall(pwd = password)
            print ('Complete')
            print 'Password:',password
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
    args = parser.parse_args()
    handle = Handler(check.min, check.max, check.rule)
    
if __name__ =='__main__':
    main()
