package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)

    // Inicialización de variables
    fmt.Print("Ingrese el nombre del equipo visitante: ")
    equipoVisitanteNombre, _ := reader.ReadString('\n')
    equipoVisitanteNombre = strings.TrimSpace(equipoVisitanteNombre)

    fmt.Print("Ingrese el nombre del equipo local: ")
    equipoLocalNombre, _ := reader.ReadString('\n')
    equipoLocalNombre = strings.TrimSpace(equipoLocalNombre)

    golesEquipoVisitante := 0
    golesEquipoLocal := 0

    // Función para mostrar el marcador
    mostrarMarcador := func() {
        fmt.Printf("Marcador: %s %d vs %s %d\n", equipoVisitanteNombre, golesEquipoVisitante, equipoLocalNombre, golesEquipoLocal)
    }

    // Función para actualizar el marcador
    actualizarMarcador := func() {
        fmt.Print("¿Qué equipo anotó un gol? (visitante/local): ")
        equipo, _ := reader.ReadString('\n')
        equipo = strings.TrimSpace(strings.ToLower(equipo))
        if equipo == strings.ToLower(equipoVisitanteNombre) {
            golesEquipoVisitante++
        } else if equipo == strings.ToLower(equipoLocalNombre) {
            golesEquipoLocal++
        } else {
            fmt.Println("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.")
        }
    }

    // Mostrar el marcador inicial
    mostrarMarcador()

    // Actualizar el marcador en un bucle
    for {
        actualizarMarcador()
        mostrarMarcador()
        fmt.Print("¿Desea continuar actualizando el marcador? (si/no): ")
        continuar, _ := reader.ReadString('\n')
        continuar = strings.TrimSpace(strings.ToLower(continuar))
        if continuar != "si" {
            break
        }
    }

    fmt.Println("Marcador final:")
    mostrarMarcador()
}
