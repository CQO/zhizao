import json

lal = []

outPut = []
file_object = open("xsd.csv",'r', encoding = 'UTF-8') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型
    strArr = all_the_text.split('\n')
    strLen = len(strArr)
    print(strLen)
    for ind1 in range(strLen):
        print('进度%s/%s' % (ind1, strLen))
        tempArr = strArr[ind1].split(',')
        for ind2 in range(len(tempArr)):
            if (tempArr[ind2] != '' and tempArr[ind2] != 0 and tempArr[ind2] != '0'):
                outPut.append({"source": ind1, "target": ind2, "width": tempArr[ind2]})
    exfile = open('output4.txt', 'w', encoding = 'UTF-8')
    exfile.write(json.dumps(outPut))
    exfile.close()
finally:
    file_object.close()
