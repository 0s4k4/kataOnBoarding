try:
    open('config.txt')
except FileNotFoundError:
    print("Archivo no encontrado")