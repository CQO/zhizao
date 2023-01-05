import json
from scipy.stats import pearsonr
import pandas as pd
import csv

idList = []

outPut = []

datas=[]
with open('feature.csv',newline='') as csvfile:
    a=csv.reader(csvfile,delimiter=',')
    for i in a:
        data=[]
        for j in i:
            data.append(float(j))
        datas.append(data)

file_object = open("test.csv",'r', encoding = 'UTF-8') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型
    strArr = all_the_text.split('\n')
    strLen = len(strArr)
    print(strLen)
    for ind1 in range(strLen):
        print('进度%s/%s' % (ind1, strLen))
        strArr[ind1] = strArr[ind1].replace(', ', ' ')
        strArr[ind1] = strArr[ind1].replace('"', '')
        tempArr = strArr[ind1].split(',')
        if (tempArr and tempArr[0] and tempArr[1] != 0):
            tempArr[0] = tempArr[0].replace('\ufeff', '')
            idList.append(int(tempArr[0]))
            temp2 = []
            for item2 in tempArr[5:]:
                if (item2):
                    temp2.append(item2)
            outPut.append([int(tempArr[0]), tempArr[1], tempArr[2], tempArr[3], tempArr[4], temp2])
        else:
            break
    result={}
    for i in range(len(idList)):
        res=[]
        print(idList[i])
        for j in range(i+1,len(idList)):
            x=pearsonr(datas[idList[i]],datas[idList[j]])[0]
            if (x > 0.7):
                if (str(idList[i]) not in result):
                    result[str(idList[i])] = []
                result[str(idList[i])].append([idList[j], round(x, 2)])
    indTemp = 0
    for item in outPut:
        if (item[0] not in result):
            print(outPut[indTemp])
            del outPut[indTemp]
        indTemp += 1
    exfile = open('output4.txt', 'w', encoding = 'UTF-8')
    exfile.write(json.dumps({
        "data": outPut,
        "link": result
    }))
    exfile.close()
finally:
    file_object.close()
