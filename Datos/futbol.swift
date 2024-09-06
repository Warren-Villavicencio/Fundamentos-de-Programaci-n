import Foundation

// Inicialización de variables
print("Ingrese el nombre del equipo visitante: ", terminator: "")
let equipoVisitanteNombre = readLine() ?? ""
print("Ingrese el nombre del equipo local: ", terminator: "")
let equipoLocalNombre = readLine() ?? ""

var golesEquipoVisitante = 0
var golesEquipoLocal = 0

// Función para mostrar el marcador
func mostrarMarcador() {
    print("Marcador: \(equipoVisitanteNombre) \(golesEquipoVisitante) vs \(equipoLocalNombre) \(golesEquipoLocal)")
}

// Función para actualizar el marcador
func actualizarMarcador() {
    print("¿Qué equipo anotó un gol? (visitante/local): ", terminator: "")
    let equipo = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? ""
    if equipo == equipoVisitanteNombre.lowercased() {
        golesEquipoVisitante += 1
    } else if equipo == equipoLocalNombre.lowercased() {
        golesEquipoLocal += 1
    } else {
        print("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.")
    }
}

// Mostrar el marcador inicial
mostrarMarcador()

// Actualizar el marcador en un bucle
while true {
    actualizarMarcador()
    mostrarMarcador()
    print("¿Desea continuar actualizando el marcador? (si/no): ", terminator: "")
    let continuar = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? ""
    if continuar != "si" {
        break
    }
}

print("Marcador final:")
mostrarMarcador()
