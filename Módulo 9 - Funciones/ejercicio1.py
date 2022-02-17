#funcion para leer 3 tanques de combustible  y mueste el promedio
def gasTank(gas1, gas2, gas3):
    return (gas1+ gas2+ gas3)/3

print(f'Average: {round(gasTank(5,15,1),2)}')

def average(sum_total, count):
    return sum_total/count


def gasTank(gas1, gas2, gas3):
    return average(gas1+ gas2+ gas3,3)

print(f'Average: {round(gasTank(2,6,1),2)}')