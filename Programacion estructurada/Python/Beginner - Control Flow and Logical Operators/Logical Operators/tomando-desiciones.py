# Ejemplo: Simulador de calificaciones
# Utilizando operadores lógicos para determinar la calificación final

nota = 85
asistencia = 0.95

# Para aprobar, se necesita una nota mayor o igual a 70 y una asistencia mayor a 0.8
if nota >= 70 and asistencia > 0.8:
    print("Aprobado.")
elif nota >= 60 and asistencia > 0.8:
    print("Regular.")
else:
    print("Reprobado.")