# def sudeti_skaicius(*args):
#     return sum(args)
#
# print(sudeti_skaicius(5, 10, 15))
# print(sudeti_skaicius(100, 200, 300, 400))
#
# def sveikiti_vardus(*args):
#    res = ''
#    for name in args:
#         print(f'Labas, {name}')
# sveikiti_vardus('Jonas', 'Petras', "Bronius")
#
#
# def spausdinti_zinutes(kartai, *args, pabaiga = "!"):
#     for elem in args:
#         print(elem * kartai, pabaiga)
# spausdinti_zinutes(5, 'Hi! ', 'Bounjour ', 'Labas ', pabaiga= ':-)')
#
# print('---------------')
#
# def dauginti_skaicius(n, *args):
#     for i in args:
#         print((i + ' ')* n)
# dauginti_skaicius(3, 'Sunday', 'Mondey', 'Wednesdey')
#
#

# kwargs
# def rodyti_duomenis(**kwargs):
#     print(kwargs)
# rodyti_duomenis(pirmas =1, antras = 2, trecias = 3)
#

# funkcija registruoti naudotoja
def registruoti_naudotoja(vardas, e_pastas, **kwargs):
    for user in kwargs:
        print(vardas, e_pastas, **kwargs)
vardas = ['Boris', 'John', 'Peter']
e_pastas = ['gg@ff.lt', 'tt@kf.lt', 'ee@lf.lt']
registruoti_naudotoja(vardas, e_pastas, end='!\n')

def atspausdinti_lista(listas, **kwargs):
    for item in listas:
        print(item, **kwargs)
list_dom = ['Sunday', 'Monday', 'Thursday', 'Wednesday', 'Thirsday', 'Friday', 'Saturday']
atspausdinti_lista(list_dom, sep = "---", end = "\n")