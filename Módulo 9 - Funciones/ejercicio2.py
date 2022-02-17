#funcion que informe preciso de la mision, considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo, tanque interno

from datetime import datetime, timedelta

from datetime import datetime, timedelta

def report(hora_prelanzamiento, tiempo_vuelo, destino, tanque_externo, tanque_interno):
    # today = datetime.now()
    # tiempo_total = today + timedelta(hours=hora_prelanzamiento+tiempo_vuelo)
    # tiempo_total.strftime('%A %H:%M')
    return f"Hora Prelanzamiento: {hora_prelanzamiento} | Tiempo de Vuelo: {tiempo_vuelo} | Destino: {destino} | Tanque Externo: {tanque_externo} | Tanque Interno: {tanque_interno}"

print (report(10,51,'Mars', 100, 200))

#nueva funcion de reporte considerando lo anterior

def report(destino, *minutes, **fuel_reservoirs):
    return f"Tiempo total: {sum(minutes)} | Destino: {destino} | Total Tanques Reserva: {sum(fuel_reservoirs.values())}"

print (report('Mars', 10,51, 15, tanque_externo=100, tanque_interno=200, tanque_extra=50))

#escribe nueva funcion

def report(destino, *minutes, **fuel_reservoirs):
    reporte = f"Tiempo total: {sum(minutes)} | Destino: {destino} | Total Tanques Reserva: {sum(fuel_reservoirs.values())}"
    for key, value in fuel_reservoirs.items():
        reporte += f'\n{key.capitalize()} = {value}'
    return reporte

print (report('Mars', 10,51, 15, tanque_externo=100, tanque_interno=200, tanque_extra=50))



