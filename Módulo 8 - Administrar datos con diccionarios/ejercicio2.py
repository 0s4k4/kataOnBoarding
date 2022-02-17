#planetas y lunas

from numpy import average


planets_moon = {
    'mercury' : 0,
    'venus' : 0,
    'earth' : 1,
    'mars' : 2,
    'jupiter' : 79,
    'saturn' : 82,
    'uranus' : 27,
    'neptune' : 14,
    'pluton' : 5,
    'haumea' : 2,
    'makemake': 1,
    'eris' : 1
}

#añadir el codigo  para determinar el numero de lunas
moons = planets_moon.values()
planets = len(planets_moon)
print(moons)
print(planets)

#agregamos el codigo  para contar  el numero de lunas

total_moons = 0
for moon in moons:
    total_moons += moon
average = total_moons /planets
print(f'Average: {average}')

