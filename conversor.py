cantidad = float(input("Ingrese la cantidad: "))

conversiones = {
    "pulgada": 2.54,
    "centímetro": 1,
    "pie": 30.48,
    "metro": 100,
    "libra": 0.45359237,
    "kilogramo": 1
}

unidades = [
    ("pulgada", "a"),
    ("centímetro", "b"),
    ("pie", "c"),
    ("metro", "d"),
    ("libra", "e"),
    ("kilogramo", "f")
]

print("Unidades de medida disponibles:")
for unidad, inciso in unidades:
    print(f"{inciso}: {unidad}")
inciso = input("Ingrese el inciso de la unidad de origen: ")

unidad_origen = None
for unidad, inciso_registrado in unidades:
    if inciso_registrado == inciso:
        unidad_origen = unidad
        break

if unidad_origen is None:
    print("La unidad de origen ingresada es inválida.")
    exit()

print("Unidades de medida disponibles:")
for unidad, inciso in unidades:
    print(f"{inciso}: {unidad}")
inciso = input("Ingrese el inciso de la unidad de destino: ")

unidad_destino = None
for unidad, inciso_registrado in unidades:
    if inciso_registrado == inciso:
        unidad_destino = unidad
        break

if unidad_destino is None:
    print("La unidad de destino ingresada es inválida.")
    exit()

factor = conversiones[unidad_origen] / conversiones[unidad_destino]
resultado = cantidad * factor
print(f"{cantidad} {unidad_origen} son {resultado} {unidad_destino}")


