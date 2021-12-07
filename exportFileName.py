flag = True
fileNames = []

while(flag):
    fileName = input('파일 명 : ')
    if fileName.upper() == 'END':
        flag = False
    else :
        fileNames.append(fileName.upper())

for file in fileNames:
    print(f'{file}', end=',')