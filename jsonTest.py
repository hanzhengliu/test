import json

f = open(r'F:\Python\学习文件保存\练习\ta1.txt','r',encoding='utf-8')
content = f.read()
#print("--------------------"+content)
#print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#json进行编码
#dumps = json.dumps(content) #特殊字符会被编码，非utf-8而是Unicode
dumps = json.loads(content.encode('utf-8')[3:].decode('utf-8'))
print(dumps)
