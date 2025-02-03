# from datetime import datetime
# import datetime
# print(datetime)
# print(datetime.today)
# # import datetime
#
# dt_res = datetime.datetime.today()
# print(dt_res)
# print(dt_res.year)
# print(dt_res.month)
# for i in range(1, 1000000):
#     a = 123
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
# print(dt_res.microsecond)
# print(f'End - {datetime.datetime.today()}')

from _datetime import datetime

dt_res = datetime.today()
year = (dt_res.year)
month = (dt_res.month)
day = (dt_res.day)
hour = (dt_res.hour)
min = (dt_res.minute)
sec = (dt_res.second)

print(year)
print(month)
print(day)
print(hour)
print(min)
print(sec)
print(f'Dabar yra {hour} : {min}, {day} - {month} - {year}')