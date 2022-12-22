conversiones = {
    "pulgada": 2.54,
    "centímetro": 1,
    "pie": 30.48,
    "metro": 100,
    "libra": 0.45359237,
    "kilogramo": 1
}

cantidad = float(input("Ingrese la cantidad: "))
unidad_origen = input("Ingrese la unidad de origen: ")
unidad_destino = input("Ingrese la unidad de destino: ")

factor = conversiones[unidad_origen] / conversiones[unidad_destino]
resultado = cantidad * factor
print(f"{cantidad} {unidad_origen} son {resultado} {unidad_destino}")
