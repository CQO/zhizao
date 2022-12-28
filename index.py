import json

lal = ['2678', '7818', '8959', '56', '671', '3239', '5305', '5710', '887', '2131', '2153', '2422', '2639', '3483', '3788', '3795', '3832', '4465', '6107', '8256', '8763', '9851', '1174', '1612', '1679', '2984', '3478', '3708', '4930', '5153', '6109', '6185', '6961', '7848', '9169', '10170', '10358', '548', '1145', '1367', '1703', '2473', '5006', '5979', '6632', '7371', '9670', '10149', '10675', '102']

outPut = {}
file_object = open("test.csv",'r', encoding = 'UTF-8') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型

    strArr = all_the_text.split('\n')
    print(strArr[0])
    for item in strArr:
        temp = item.split(',')
        if (temp[0] and str(int(temp[0])) in lal):
            outPut[str(int(temp[0]))] = temp
    exfile = open('output3.txt', 'w', encoding = 'UTF-8')
    exfile.write(json.dumps(outPut))
    exfile.close()
finally:
    file_object.close()
