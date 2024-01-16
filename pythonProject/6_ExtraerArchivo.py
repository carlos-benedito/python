nombre_archivo = input("Introduce el nombre del archivo con extensión: ")


nombre_sin_extension, extension = nombre_archivo.split('.', 1)


print("Extensión del archivo:", extension)