import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django

django.setup()

from MainApp.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

print("")
print("**************")
print("")

p = Pizza.objects.get(id=4)
print(p.name)
print(p.date_added)

print("")

toppings = p.topping_set.all()

for topping in toppings:
    print(topping)
