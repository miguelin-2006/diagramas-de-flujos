'''
Algoritmo: Control de stock semanal
Entrada: stock_inicial, ventas (por día)
Salida: stock_final, pedidos
bloque de desarrollo:
    LEER stock
    pedidos = 0
    PARA dia DESDE 1 HASTA 7:
        LEER ventas
        stock = stock - ventas
        SI stock < 10:
            ESCRIBIR "Reponer día ", dia
            stock = stock + 50
            pedidos = pedidos + 1
    ESCRIBIR stock, pedidos
'''

def control_stock(stock_inicial, ventas_semanales):
    stock = stock_inicial
    pedidos = 0
    
    for dia in range(1, 8):
        ventas = ventas_semanales[dia - 1]
        stock -= ventas
        if stock < 10:
            print(f"Reponer en el día {dia}")
            stock += 50
            pedidos += 1
            
    return stock, pedidos

# Prueba con los datos del cuaderno
ventas_ejemplo = [12, 15, 8, 20, 5, 18, 9]
stock_final, total_pedidos = control_stock(40, ventas_ejemplo)

print(f"\nStock final: {stock_final}")
print(f"Total pedidos realizados: {total_pedidos}")