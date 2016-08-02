import os
import shutil
import time
import random
from sys import argv

class FileExec:
    filepath='/home/user/python/random.txt'

    def create_random_file():
            print(*random.sample(range(1,1001,2),100),file=open(filepath,'a'))
            ctime= os.path.getctime('random.txt')
            mtime= os.path.getmtime('random.txt')
            print(time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(ctime),file=open(filepath,'a'))
            print(time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(mtime),file=open(filepath,'a'))   
            local=os.getcwd() 

            os.mkdir(local+'/test')
            shutil.move('random.txt','.\\test\\random.txt')


if __name__ == '__main__':
    FileExec.random_odd()