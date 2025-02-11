# class Darbuotojai:
#     def __str__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#
#     def change_employee_name(self, vardas):
#         if not vardas:
#             raise ValueError('Name is not provided')
#
#         self.vardas = vardas
#
#     @staticmethod
#     def devide(a, b):
#         if b == 0:
#             raise  ZeroDivisionError('Cant be devided by zero')
#         return a / b
#
#     @classmethod
#     def super_constructor(cls, vardas, pavarde, pareigos):
#         return cls(vardas, pavarde, pareigos)
#
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home page</h>"
if __name__