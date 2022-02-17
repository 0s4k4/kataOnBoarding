# Escribe el ciclo while solicitado

new_planet =''
planets = []

while new_planet!='done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Please enter a planet name, or done if done ')


for planet in planets:
    print(planet)