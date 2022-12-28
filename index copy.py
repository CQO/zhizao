import json

def lala (key):
    return key['value']

file_object = open("list.txt",'r', encoding = 'UTF-8') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型
    strArr = json.loads(all_the_text)
    print(strArr[0])
    strArr.sort(key=lala,reverse=True)
    print(strArr[0:50])
    # return
    # exfile = open('output2.txt', 'w', encoding = 'UTF-8')
    # exfile.write(key_list)
    # exfile.close()
finally:
    file_object.close()
