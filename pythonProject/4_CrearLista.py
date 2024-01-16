
entrada_usuario = input("Introduce un conjunto de números separados por coma: ")
numeros_str = entrada_usuario.split(',')
numeros_lista = [int(numero) for numero in numeros_str]
print("Lista de números:", numeros_lista)