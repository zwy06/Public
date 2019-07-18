"""
存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头
"""
# city01 = [{"北京":[{"景区":["故宫","天安门","天坛"]},
#                   {"美食": ["烤鸭","炸酱面","豆汁","卤煮"]}]},
#            {"四川":[{"景区":["九寨沟","峨眉山","春熙路"]},
#             {"美食": ["火锅","串串香","兔头"]}]}]
#
# for location in city01:
#     for city_info, category_info in location.items():
#         print(city_info+":")
#         for introduce in category_info:
#             for category,category_value in introduce.items():
#                 #for item_location in category_value
#                 print("\t%s: %s %s %s" % (category,category_value[0],category_value[1],category_value[2]))
#


city02 = {"北京":{"景区":["故宫","天安门","天坛"],
                  "美食": ["烤鸭","炸酱面","豆汁","卤煮"]},
           "四川":{"景区":["九寨沟","峨眉山","春熙路"],
            "美食": ["火锅","串串香","兔头"]}}
# 所有城市的景区
list01 =[]
for key in city02:
    # print(key)
    for item in city02[key]["美食"]:
        # print(item)
        print(list01.append(key + ":" +item))