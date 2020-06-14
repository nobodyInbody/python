# -*- coding:utf-8 -*-
import os
import sys
import datetime

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

def addDateFile(fileArgv):
    fileObj = fileArgv
    fileDirname = os.path.dirname(fileObj)
    fileName =  os.path.basename(fileObj)
    todayobj = str(datetime.date.today())
    alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i = 0
    date_list = todayobj.split('-') # = [2018, 1, 26]
    while i < (len(alpha_list)-1) :
        fileName_New = str(date_list[0]) + '_' + str(date_list[1]) + '_' + str(date_list[2]) + '_' + str(alpha_list[i]) + '__' + fileName
        #fileName_New = unicode(date_list[0]) + '_' + unicode(date_list[1]) + '_' + unicode(date_list[2]) + '_' + unicode(alpha_list[i]) + '__' + fileName
        reNameFile = os.path.join(fileDirname, fileName_New)
        print('reNameFile', reNameFile)
        try:
            os.rename(fileArgv,reNameFile)
            break
        except:
            i = i + 1


def main():
    #print ('version is', sys.version)
    #print ('argv', sys.argv)
    #print (os.getcwd())
    filelist = sys.argv[1:]
    #print ('filelist', filelist)
    for i in filelist:
        addDateFile(i)


if __name__ == '__main__':
    main()


