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


def spausdinti_zinutes(kartai, *args, pabaiga = "!"):
    for elem in args:
        print(elem * kartai, pabaiga)
spausdinti_zinutes(5, 'Hi! ', 'Bounjour ', 'Labas ', pabaiga= ':-)')

print('---------------')

def dauginti_skaicius(n, *args):
    for i in args:
        print((i + ' ')* n)
dauginti_skaicius(3, 'Sunday', 'Mondey', 'Wednesdey')



