'''
Algoritmo: Gastos de envío
Entrada: importe, peso
Salida: envio, total
bloque de desarrollo:
    LEER importe, peso
    SI importe >= 50:
        envio = 0
    SI NO SI peso > 5:
        envio = 9.95
    SI NO:
        envio = 4.95
    total = importe + envio
    ESCRIBIR envio, total
'''

def calcular_gastos_envio(importe, peso):
    if importe >= 50:
        envio = 0
    elif peso > 5:
        envio = 9.95
    else:
        envio = 4.95
    
    total = importe + envio
    return envio, total

# Pruebas
print("Resultado para calcular_gastos_envio(30, 8):")
e, t = calcular_gastos_envio(30, 8)
print(f"Envío: {e} €, Total: {t} €")