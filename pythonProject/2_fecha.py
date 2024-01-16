from datetime import datetime


fecha_actual = datetime.now()


fecha_ingresada_str = input("Introduce una fecha en formato YYYY-MM-DD: ")
fecha_ingresada = datetime.strptime(fecha_ingresada_str, "%Y-%m-%d")

diferencia_en_dias = (fecha_actual - fecha_ingresada).days
print(f"La diferencia en días entre {fecha_ingresada_str} y hoy es: {diferencia_en_dias} días.")