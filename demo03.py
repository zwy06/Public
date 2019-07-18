"""
    字典 dict

#1.创建
# 空
# dict01 = {}
dict01 = dict()
# 默认值
dict01 = {"wj":100,"zm":80,"zr":90}
dict02 = dict([("a","b"),("c","d")])
print(dict01)
print(dict02)
#2.查找元素(根据key查找value)
print(dict02["a"])
#如果键不存在,查找时会报错
if "qtx" in dict01:
    print(dict02["qtx"])
#3.修改(之前存在key)
dict02["a"] = "BB"
#4.添加(之前不存在key)
dict02["e"] = "f"
#5.删除
del dict02["a"]
#6.遍历字典,得到的是key
for key in dict01:
    print(key)
    print(dict01[key])
#7.遍历字典,获取value
for value in dict01.values():
    print(value)
#7.遍历字典,获取键值对key,value
for item in dict01.items():
    print(item)
#7.遍历字典,分开获取key,value
for a,b in dict01.items():
    print(a)
    print(b)
"""
"""
    练习1.在控制台中循环录入商品信息(名称,单价)
    如果名称输入空字符,则停止录入
    
dict_message ={}
while True:
    name = input("请输入商品信息:")
    if name == "":
        break
    pecies = int(input("请输入商品单价:"))
    dict_message[name] = pecies
for key,value in dict_message.items():
    print("%s单价是%d" % (key,value))
"""
"""
    练习1.在控制台中循环录入学生信息(姓名,年龄,成绩,性格)
    如果名称输入空字符,则停止录入
#字典内嵌列表
dict_message ={}
while True:
    name = input("请输入姓名信息:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    charge = int(input("请输入成绩:"))
    xingge = input("请输入性别:")
    dict_message[name]= [age,charge,xingge]
for key,list_info in dict_message.items():
    print("%s的年龄是%d,成绩是%d,性别是:%s"% (key,list_info[0],list_info[1],list_info[2]))

#字典内嵌字典
dict_message ={}
while True:
    name = input("请输入姓名信息:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    dict_message[name]= {"age":age,"score":score, "sex":sex}
for name, dict_info in dict_message.items():
    print("%s的年龄是%d,成绩是%d,性别是:%s" % (name, dict_info["age"], dict_info["score"], dict_info["sex"]))
"""
#列表内嵌字典
list_student_info =[]
while True:
    name = input("请输入姓名信息:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    list_student_info.append({"name":name, "age":age, "score":score, "sex":sex})
for dict_info in list_student_info:
    print("%s的年龄是%d,成绩是%d,性别是:%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
#第一个的信息
dict_info = list_student_info[0]
print("第一个人的信息是:%s的年龄是%d,成绩是%d,性别是:%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))


