# Crea un diccionario llamado planet con los datos propuestos
planet = {
    'name': 'Mars',
    'moons': 2
}

#mostrar el planeta
print(f"Planet {planet['name']} with {planet.get('moons')} moons")

#agregar la clave circuferencia  con los datos  proporcionados previamentw
planet.update({
    'circunferencia (km)': {
        'polar': 6752,
        'equatorial': 6792
    }
})
print (planet)


print(f"Planet {planet['name']} with circunference: {planet.get('circunferencia (km)').get('polar')} polar") 
print(f"and {planet.get('circunferencia (km)').get('equatorial')} equatorial ")