'''
Algoritmo: Duración de un viaje
Entrada: distancia, velocidad
Salida: horas, resto
bloque de desarrollo:
    LEER distancia
    LEER velocidad
    minutos = redondear((distancia / velocidad) * 60)
    horas = minutos // 60
    resto = minutos % 60
    ESCRIBIR horas, "h", resto, "min"
'''

def duracion_viaje(distancia, velocidad):
    minutos = round((distancia / velocidad) * 60)
    horas = minutos // 60
    resto = minutos % 60
    return horas, resto

# Pruebas
print("Resultado para duracion_viaje(350, 100):")
h, m = duracion_viaje(350, 100)
print(f"{h} h {m} min")