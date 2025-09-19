"""
El propósito de este programa es dado 3 números dados, este los organiza de acuerdo de mayor a menor
Eduardo Caleb Castillo Llanas 18/Sep/25
"""
# Declaraciones
numeros = []

# Entradas
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))

# Proceso
numeros.sort(reverse=True)

# Salidas
print(numeros)
