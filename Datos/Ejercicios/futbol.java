import java.util.Scanner;

public class Futbol {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Inicialización de variables
        System.out.print("Ingrese el nombre del equipo visitante: ");
        String equipoVisitanteNombre = scanner.nextLine();
        System.out.print("Ingrese el nombre del equipo local: ");
        String equipoLocalNombre = scanner.nextLine();

        int golesEquipoVisitante = 0;
        int golesEquipoLocal = 0;

        // Función para mostrar el marcador
        mostrarMarcador(equipoVisitanteNombre, golesEquipoVisitante, equipoLocalNombre, golesEquipoLocal);

        // Actualizar el marcador en un bucle
        while (true) {
            System.out.print("¿Qué equipo anotó un gol? (visitante/local): ");
            String equipo = scanner.nextLine().trim().toLowerCase();
            if (equipo.equals(equipoVisitanteNombre.toLowerCase())) {
                golesEquipoVisitante++;
            } else if (equipo.equals(equipoLocalNombre.toLowerCase())) {
                golesEquipoLocal++;
            } else {
                System.out.println("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.");
            }

            mostrarMarcador(equipoVisitanteNombre, golesEquipoVisitante, equipoLocalNombre, golesEquipoLocal);

            System.out.print("¿Desea continuar actualizando el marcador? (si/no): ");
            String continuar = scanner.nextLine().trim().toLowerCase();
            if (!continuar.equals("si")) {
                break;
            }
        }

        System.out.println("Marcador final:");
        mostrarMarcador(equipoVisitanteNombre, golesEquipoVisitante, equipoLocalNombre, golesEquipoLocal);
    }

    public static void mostrarMarcador(String equipoVisitanteNombre, int golesEquipoVisitante, String equipoLocalNombre, int golesEquipoLocal) {
        System.out.println("Marcador: " + equipoVisitanteNombre + " " + golesEquipoVisitante + " vs " + equipoLocalNombre + " " + golesEquipoLocal);
    }
}
