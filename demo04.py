
"""
    需求:存储多个学生信息(姓名,性别,年龄,成绩)
    字典内嵌列表:

    字典内嵌字典:

    列表内嵌字典:

选择策略:根据具体需求,结合优缺点,综合考虑
    字典:
        优点:根据键获取值所以读取速度快;
            代码可读性相对列表更高(根据键获取比根据索引获取)
        缺点:内存占用大
            获取值只能根据键,不灵活
    列表:
        优点:根据索引/切片,获取元素更灵活
            相比字典占内存更小
        缺点:通过索引获取,如果信息较多,可读性不高

"""
#练习:在控制台中录入多个人的多个喜好
# 例如:请输入姓名:
# 请输入第一个喜好:
# 请输入第二个喜好:
# 空格不输入喜好
# 最后在空格退出
# 最后在控制台打印所有人的所有喜好
"""
字典内嵌列表
{name:[hobby1,hobby2,hobby3]}
"""
dict_hobby ={}
while True:
    name = input("请输入姓名:")
    if name =="":
        break
    dict_hobby[name] = []
    while True:
        hobby = input("请输入爱好:")
        if hobby =="":
            break
        dict_hobby[name].append(hobby)
for key,value in dict_hobby.items():
    print("%s喜欢:" % (key))
    for item in value:
        print(item)
"""
字典内嵌列表
{[name:[hobby1,hobby2,hobby3]]}
"""




