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
#
# from _datetime import datetime
#
# dt_res = datetime.today()
# year = (dt_res.year)
# month = (dt_res.month)
# day = (dt_res.day)
# hour = (dt_res.hour)
# min = (dt_res.minute)
# sec = (dt_res.second)
#
# print(year)
# print(month)
# print(day)
# print(hour)
# print(min)
# print(sec)
#
# print(f'Dabar yra {hour} : {min}, {day} - {month} - {year}')
#
# my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
# today_dt = datetime.datetime.today()
# print(my_datetime)
#
# if my_datetime < today_dt:
#     print('YES')
#
# def is_save_still_valid(start_dt, end_dt) -> bool:
#     today_dt = datetime.datetime.today()
#     if start_dt < today_dt < end_dt:
#         return True
#     return False
#
# sale_start_dt = datetime.datetime(2025, 2, 2)
# sale_end_dt = datetime.datetime(2025, 5, 2)
#
# is_still_valid = is_save_still_valid((sale_start_dt, sale_end_dt))
# if not is_still_valid:
#     raise ValueError('Sale is over')
#
# print('Thank you for buying')

# from _datetime import datetime
# dt_obj = datetime(1995, 7, 14, 15, 30, 00)
# print(f"{dt_obj:%Y-%m-%d}")
# dt_obj2 = datetime(2023, 1, 1)
# print(f"{dt_obj2:%Y-%m-%d}")
import datetime
# ivestis = '2020-02-11'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
# print(my_datetime)
# print(my_datetime.strftime('%Y-%m-%d'))
# print(my_datetime.strftime('%Y-%B-%d'))

# import datetime
#
# # 1
# liepos_15 = datetime.datetime(1995, 7, 14, 15, 30)
# print(liepos_15)
# dt_without_time = datetime.datetime(2023, 1, 1)
# print(dt_without_time)
#
# # 2
# dt_today = datetime.datetime.today()
# metai_2000 = datetime.datetime(2000, 1, 1)
# print(f'Praėjo {(dt_today - metai_2000).days} dienų nuo 2000-01-01.')

# import datetime
# vartotojo_ivestis = input('Please enter date in format "YYYY-MM-DD":')
# dt_obj = datetime.datetime.strptime(vartotojo_ivestis, '%Y-%m-%d')
# print(dt_obj)


# import datetime
# dt_obj = '2022-12-31, 23:59:59'
# data = datetime.datetime.strptime(dt_obj, '%Y-%m-%d, %H:%M:%S')
# print(data)

#

# ivestis = '2022-12-31, 23:59:59'
# date_time = datetime.datetime.strptime(ivestis, '%Y-%m-%d, %H:%M:%S')
#
# formated_date_time_1 = date_time.strptime('%d/%m/%Y, %H:%M:%S')
# print(formated_date_time_1)
# ivestis = '2020-02-11'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
# print(my_datetime)
# print(my_datetime.strftime('%Y-%m-%d'))
# print(my_datetime.strftime('%Y-%B-%d'))
#
# from datetime import datetime
#
# ivesta_data = input("Įveskite datą formatu 'YYYY-MM-DD': ")
#
# while True:
#     try:
#         data_obj = datetime.strptime(ivesta_data, "%Y-%m-%d")
#         print("Įvesta data datetime formatu:", data_obj)
#         break
#     except ValueError:
#         print("Neteisingas datos formatas. Prašome įvesti datą teisingu formatu.")
#
# data_laikas = datetime(2022, 12, 31, 23, 59, 59)
#
# formatted_1 = data_laikas.strftime("%d/%m/%Y %H:%M:%S")
# print(formatted_1)
#
# menesiai = {
#     1: "sausio", 2: "vasario", 3: "kovo", 4: "balandžio",
#     5: "gegužės", 6: "birželio", 7: "liepos", 8: "rugpjūčio",
#     9: "rugsėjo", 10: "spalio", 11: "lapkričio", 12: "gruodžio"
# }
#
# formatted_2 = f"{data_laikas.year} metų {menesiai[data_laikas.month]} {data_laikas.day} diena"
# print(formatted_2)
#
#
#

# Užduotis 7:
# 1. Sukurkite dvi datas:
# a. 2023-01-01
# b. 2024-01-01
# 2. Apskaičiuokite laiko skirtumą tarp jų naudojant - operatorių.
# 3. Išveskite rezultatą dienomis.

import datetime
data1 = datetime.datetime(2023, 1, 1)
print(data1)
data2 = datetime.datetime(2024, 1, 1)
print(data2)
skirtumas = data2 - data1
print(skirtumas.days)
print('--------------')
# Užduotis 8:
# 1. Sukurkite programą, kuri:
# a. Naudoja dabartinę datą.
# b. Prideda 90 dienų naudojant timedelta.
# 2. Išveskite rezultatą:
# "Data po 90 dienų bus: <data>"

data_now = datetime.datetime.today()
skirtumas = datetime.timedelta(days=90)
res = data_now + skirtumas
print(f'Data po 90 dienus bus: {res}')

print('--------------')
# Užduotis 9:
# 1. Apskaičiuokite skirtumą tarp 2000-01-01 ir šiandienos.
# 2. Išveskite:
# a. Dienų skaičių
# b. Valandų skaičių (naudojant .seconds)
# c. Bendrą sekundžių skaičių (.total_seconds())

data_2000 = datetime.datetime(2000, 1, 1)
data_now = datetime.datetime.today()
skirtumas = data_now - data_2000
print(f'Skirtumas dienomis: {skirtumas.days}')
print(f'Skirtumas sekundemis: {skirtumas.seconds}')
print(f'Bendras sekundziu skaicius: {skirtumas.total_seconds()}')