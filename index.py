import os
import shutil
import subprocess

if os.environ.get("TableLayoutPathByJYLIM") is None:
    envPath = input("Table Layout 위치를 입력해주세요 : ")
    subprocess.run(f'$Env:TableLayoutPathByJYLIM {envPath}')

if os.environ.get("TableLayoutDirByJYLIM") is None:
    envDir = input("Table Layout을 옮길 위치를 입력해주세요 : ")
    subprocess.run(f'$Env:TableLayoutDirByJYLIM {envDir}')

isSearched = False

path = os.environ.get("TableLayoutPathByJYLIM")
dir = os.environ.get("TableLayoutDirByJYLIM")

tableName = input('테이블 이름을 입력해주세요 : ').upper()

fileNameArr = tableName.split(',')

isPersent = False

for idx, i in enumerate(fileNameArr, 0):
    lastText = i.__len__() - 1

    if i[lastText] is '%':
        fileNameArr[idx] = i.split('%')[0]
        isPersent = True

file_list = os.listdir(path)

for i in file_list :
    for file in fileNameArr:
        if file in i and isPersent:
            print(i)
            shutil.copy(path + i, dir + i)
            isSearched = True
        elif file + ".xlsx" in i:
            print(i)
            shutil.copy(path + i, dir + i)
            isSearched = True

if isSearched is False :
    print(tableName + ' 테이블을 찾지 못했습니다.')