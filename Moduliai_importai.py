# import random
# atsitiktinis_skaicius = random.randint(1,10)
# print(f'Atsitiktinis skaicius:{atsitiktinis_skaicius}')

# import random
# atsitiktinis_randint = random.randint(1, 100)
# print(f'Atsitiktinis skaicius:{atsitiktinis_randint}')
#
# atsitiktinis_uniform = round(random.uniform(1, 50))
# print(f'Atsitiktinis skaicius:{atsitiktinis_uniform}')
#
# from random import randint, choice
#
# random_number = randint(1, 10)
# print(random_number)
# random_month = choice(['sausis', 'vasaris', 'kovas'])
# print(random_month)

# import random as rn
# random_number = rn.randint(20,25)
# random_month = rn.choice(['sausis', 'vasaris', 'kovas'])
# print(random_month)


from random import randint, choice
random_number = randint(1, 10)
random_fruit = choice(['obuolys', 'bananas', 'kriause', 'vysnia'])
print(random_number)
print(random_fruit)

import datetime
data_now  = datetime.datetime.now()
print(data_now)