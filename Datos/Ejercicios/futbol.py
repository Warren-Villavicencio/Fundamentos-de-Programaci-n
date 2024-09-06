# Inicialización de variables
equipo_visitante_nombre = input("Ingrese el nombre del equipo visitante: ")
equipo_local_nombre = input("Ingrese el nombre del equipo local: ")

goles_equipo_visitante = 0
goles_equipo_local = 0

# Función para mostrar el marcador
def mostrar_marcador():
    print(f"Marcador: {equipo_visitante_nombre} {goles_equipo_visitante} vs {equipo_local_nombre} {goles_equipo_local}")

# Función para actualizar el marcador
def actualizar_marcador():
    global goles_equipo_visitante, goles_equipo_local
    equipo = input("¿Qué equipo anotó un gol? (visitante/local): ").strip().lower()
    if equipo == equipo_visitante_nombre:
        goles_equipo_visitante += 1
    elif equipo == equipo_local_nombre:
        goles_equipo_local += 1
    else:
        print("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.")

# Mostrar el marcador inicial
mostrar_marcador()

# Actualizar el marcador en un bucle
while True:
    actualizar_marcador()
    mostrar_marcador()
    continuar = input("¿Desea continuar actualizando el marcador? (si/no): ").strip().lower()
    if continuar != "si":
        break

print("Marcador final:")
mostrar_marcador()
