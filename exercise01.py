"""
    将1970年到2050年中的闰年，存入列表
"""
# list_year = []
# for year in range(1970,2051):
#     if year %4 ==0 and year %100 !=0 or year %400 ==0:
#         list_year.append(year)
# print(list_year)

list_year = [year for year in range(1970,2051) if year %4 ==0 and year %100 !=0 or year %400 ==0 ]
print(list_year)