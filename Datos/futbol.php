<?php
// Inicialización de variables
echo "Ingrese el nombre del equipo visitante: ";
$equipoVisitanteNombre = trim(fgets(STDIN));
echo "Ingrese el nombre del equipo local: ";
$equipoLocalNombre = trim(fgets(STDIN));

$golesEquipoVisitante = 0;
$golesEquipoLocal = 0;

// Función para mostrar el marcador
function mostrarMarcador($equipoVisitanteNombre, $golesEquipoVisitante, $equipoLocalNombre, $golesEquipoLocal) {
    echo "Marcador: $equipoVisitanteNombre $golesEquipoVisitante vs $equipoLocalNombre $golesEquipoLocal\n";
}

// Función para actualizar el marcador
function actualizarMarcador(&$golesEquipoVisitante, &$golesEquipoLocal, $equipoVisitanteNombre, $equipoLocalNombre) {
    echo "¿Qué equipo anotó un gol? (visitante/local): ";
    $equipo = trim(fgets(STDIN));
    if (strtolower($equipo) == strtolower($equipoVisitanteNombre)) {
        $golesEquipoVisitante++;
    } elseif (strtolower($equipo) == strtolower($equipoLocalNombre)) {
        $golesEquipoLocal++;
    } else {
        echo "Entrada no válida. Por favor, ingrese 'visitante' o 'local'.\n";
    }
}

// Mostrar el marcador inicial
mostrarMarcador($equipoVisitanteNombre, $golesEquipoVisitante, $equipoLocalNombre, $golesEquipoLocal);

// Actualizar el marcador en un bucle
while (true) {
    actualizarMarcador($golesEquipoVisitante, $golesEquipoLocal, $equipoVisitanteNombre, $equipoLocalNombre);
    mostrarMarcador($equipoVisitanteNombre, $golesEquipoVisitante, $equipoLocalNombre, $golesEquipoLocal);
    echo "¿Desea continuar actualizando el marcador? (si/no): ";
    $continuar = trim(fgets(STDIN));
    if (strtolower($continuar) != "si") {
        break;
    }
}

echo "Marcador final:\n";
mostrarMarcador($equipoVisitanteNombre, $golesEquipoVisitante, $equipoLocalNombre, $golesEquipoLocal);
?>
