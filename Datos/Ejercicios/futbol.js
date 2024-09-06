// Inicialización de variables
const equipoVisitanteNombre = prompt("Ingrese el nombre del equipo visitante:");
const equipoLocalNombre = prompt("Ingrese el nombre del equipo local:");

let golesEquipoVisitante = 0;
let golesEquipoLocal = 0;

// Función para mostrar el marcador
function mostrarMarcador() {
    console.log(`Marcador: ${equipoVisitanteNombre} ${golesEquipoVisitante} vs ${equipoLocalNombre} ${golesEquipoLocal}`);
}

// Función para actualizar el marcador
function actualizarMarcador() {
    const equipo = prompt("¿Qué equipo anotó un gol? (visitante/local):").trim().toLowerCase();
    if (equipo === equipoVisitanteNombre.toLowerCase()) {
        golesEquipoVisitante += 1;
    } else if (equipo === equipoLocalNombre.toLowerCase()) {
        golesEquipoLocal += 1;
    } else {
        console.log("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.");
    }
}

// Mostrar el marcador inicial
mostrarMarcador();

// Actualizar el marcador en un bucle
while (true) {
    actualizarMarcador();
    mostrarMarcador();
    const continuar = prompt("¿Desea continuar actualizando el marcador? (si/no):").trim().toLowerCase();
    if (continuar !== "si") {
        break;
    }
}

console.log("Marcador final:");
mostrarMarcador();
