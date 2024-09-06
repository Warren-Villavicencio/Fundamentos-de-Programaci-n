# Inicialización de variables
print "Ingrese el nombre del equipo visitante: "
equipo_visitante_nombre = gets.chomp
print "Ingrese el nombre del equipo local: "
equipo_local_nombre = gets.chomp

goles_equipo_visitante = 0
goles_equipo_local = 0

# Función para mostrar el marcador
def mostrar_marcador(equipo_visitante_nombre, goles_equipo_visitante, equipo_local_nombre, goles_equipo_local)
  puts "Marcador: #{equipo_visitante_nombre} #{goles_equipo_visitante} vs #{equipo_local_nombre} #{goles_equipo_local}"
end

# Función para actualizar el marcador
def actualizar_marcador(equipo_visitante_nombre, equipo_local_nombre, goles_equipo_visitante, goles_equipo_local)
  print "¿Qué equipo anotó un gol? (visitante/local): "
  equipo = gets.chomp.downcase
  if equipo == equipo_visitante_nombre.downcase
    goles_equipo_visitante += 1
  elsif equipo == equipo_local_nombre.downcase
    goles_equipo_local += 1
  else
    puts "Entrada no válida. Por favor, ingrese 'visitante' o 'local'."
  end
  return goles_equipo_visitante, goles_equipo_local
end

# Mostrar el marcador inicial
mostrar_marcador(equipo_visitante_nombre, goles_equipo_visitante, equipo_local_nombre, goles_equipo_local)

# Actualizar el marcador en un bucle
loop do
  goles_equipo_visitante, goles_equipo_local = actualizar_marcador(equipo_visitante_nombre, equipo_local_nombre, goles_equipo_visitante, goles_equipo_local)
  mostrar_marcador(equipo_visitante_nombre, goles_equipo_visitante, equipo_local_nombre, goles_equipo_local)
  print "¿Desea continuar actualizando el marcador? (si/no): "
  continuar = gets.chomp.downcase
  break unless continuar == "si"
end

puts "Marcador final:"
mostrar_marcador(equipo_visitante_nombre, goles_equipo_visitante, equipo_local_nombre, goles_equipo_local)
