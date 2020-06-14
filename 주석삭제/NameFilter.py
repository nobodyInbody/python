# -*- coding:utf-8 -*-
import os
import sys

#주석제거

def removeName(fileArgv):
    fileObj = fileArgv
    fileDirname = os.path.dirname(fileObj)
    fileName =  os.path.basename(fileObj)
    obj = os.path.splitext(fileName)
    name = obj[0].split(',')
    fileName = str(name[0]) +  str(obj[1])
    reNameFile = os.path.join(fileDirname, fileName)
    try:
        os.rename(fileArgv,reNameFile)
    except:
        print(u"중복된 파일명이 존제하는것 같습니다.")
        os.system('Pause')

def main():
    #print ('version is', sys.version)
    #print ('argv', sys.argv)
    #print (os.getcwd())
    filelist = sys.argv[1:]
    #print ('filelist', filelist)
    for i in filelist:
        removeName(i)


if __name__ == '__main__':
    main()


