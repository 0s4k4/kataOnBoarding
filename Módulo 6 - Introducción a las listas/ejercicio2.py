# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
planet_input = input('Please enter the name of a planet (capitalize it): ')

# Busca el planeta en la lista
index = planets.index(planet_input)
print(index)


# Muestra los planetas más lejanos al sol
far_planets_to_sun = planets[index+1:]
print('Far planets to sun', far_planets_to_sun)