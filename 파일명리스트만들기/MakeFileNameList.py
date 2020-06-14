# -*- coding:utf-8 -*-
import os
import sys
 
def MakeFile(arg):
    fileList = arg
    target_folder_path = os.path.dirname(fileList[0])
    #print(u'출력 주소' + target_folder_path)
    target_file = open(os.path.join(target_folder_path , u"_fileNameList.txt"), "w", encoding = "UTF8")
    for obj_file in fileList:
        target_file.write(os.path.basename(obj_file) + u"\n")
        #print(os.path.basename(obj_file))
    target_file.close()

def main():
    #print ('version is', sys.version)
    #print ('argv', sys.argv)
    #print (os.getcwd())
    filelist = sys.argv[1:]
    #print ('filelist', filelist)
    if len(filelist) > 0 :
        MakeFile(filelist)

if __name__ == '__main__':
    main()
