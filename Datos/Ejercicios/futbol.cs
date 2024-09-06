using System;

class Futbol
{
    static void Main()
    {
        // Inicialización de variables
        Console.Write("Ingrese el nombre del equipo visitante: ");
        string equipoVisitanteNombre = Console.ReadLine();
        Console.Write("Ingrese el nombre del equipo local: ");
        string equipoLocalNombre = Console.ReadLine();

        int golesEquipoVisitante = 0;
        int golesEquipoLocal = 0;

        // Función para mostrar el marcador
        void MostrarMarcador()
        {
            Console.WriteLine($"Marcador: {equipoVisitanteNombre} {golesEquipoVisitante} vs {equipoLocalNombre} {golesEquipoLocal}");
        }

        // Función para actualizar el marcador
        void ActualizarMarcador()
        {
            Console.Write("¿Qué equipo anotó un gol? (visitante/local): ");
            string equipo = Console.ReadLine().Trim().ToLower();
            if (equipo == equipoVisitanteNombre.ToLower())
            {
                golesEquipoVisitante++;
            }
            else if (equipo == equipoLocalNombre.ToLower())
            {
                golesEquipoLocal++;
            }
            else
            {
                Console.WriteLine("Entrada no válida. Por favor, ingrese 'visitante' o 'local'.");
            }
        }

        // Mostrar el marcador inicial
        MostrarMarcador();

        // Actualizar el marcador en un bucle
        while (true)
        {
            ActualizarMarcador();
            MostrarMarcador();
            Console.Write("¿Desea continuar actualizando el marcador? (si/no): ");
            string continuar = Console.ReadLine().Trim().ToLower();
            if (continuar != "si")
            {
                break;
            }
        }

        Console.WriteLine("Marcador final:");
        MostrarMarcador