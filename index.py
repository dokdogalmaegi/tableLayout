import os
import shutil
import subprocess

if os.environ.get("TableLayoutPathByJYLIM") is None:
    envPath = input("Table Layout 위치를 입력해주세요 : ")
    subprocess.run(f'$Env:TableLayoutPathByJYLIM {envPath}')

if os.environ.get("TableLayoutDirByJYLIM") is None:
    envDir = input("Table Layout을 옮길 위치를 입력해주세요 : ")
    subprocess.run(f'$Env:TableLayoutDirByJYLIM {envDir}')

path = os.environ.get("TableLayoutPathByJYLIM")
dir = os.environ.get("TableLayoutDirByJYLIM")

isSearched = False
isPersent = False

tableName = input('테이블 이름을 입력해주세요 : ').upper()

fileNameArr = tableName.split(',')

for idx, i in enumerate(fileNameArr, 0):
    lastText = i.__len__() - 1

    if i[lastText] is '%':
        fileNameArr[idx] = i.split('%')[0]
        isPersent = True

file_list = os.listdir(path)

for file in file_list :
    for fileName in fileNameArr:
        if fileName in file and isPersent:
            print(file)
            shutil.copy(path + file, dir + file)
            isSearched = True
        elif fileName + ".xlsx" in file:
            print(file)
            shutil.copy(path + file, dir + file)
            isSearched = True

if isSearched is False :
    print(tableName + ' 테이블을 찾지 못했습니다.')