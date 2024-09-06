using System;

class OperadoresCSharp
{
    static void Main()
    {
        // Operadores de cálculo en C#

        // Suma (+)
        int a = 5 + 3;  // a = 8

        // Resta (-)
        int b = 10 - 4;  // b = 6

        // Multiplicación (*)
        int c = 3 * 4;  // c = 12

        // División (/)
        double d = 15.0 / 3;  // d = 5.0

        // Módulo (%)
        int e = 17 % 3;  // e = 2 (resto de la división)

        // Operadores de asignación en C#

        // Asignación simple (=)
        int x = 10;

        // Asignación con suma (+=)
        x += 5;  // Equivalente a: x = x + 5

        // Asignación con resta (-=)
        x -= 3;  // Equivalente a: x = x - 3

        // Asignación con multiplicación (*=)
        x *= 2;  // Equivalente a: x = x * 2

        // Asignación con división (/=)
        x /= 4;  // Equivalente a: x = x / 4

        // Asignación con módulo (%=)
        x %= 3;  // Equivalente a: x = x % 3

        // Operadores bit a bit
        int y = 5;  // 101 en binario
        y <<= 1;    // Desplazamiento a la izquierda, y = 10 (1010 en binario)
        y >>= 1;    // Desplazamiento a la derecha, y = 5 (101 en binario)
        y &= 3;     // AND bit a bit, y = 1 (001 en binario)
        y |= 4;     // OR bit a bit, y = 5 (101 en binario)
        y ^= 1;     // XOR bit a bit, y = 4 (100 en binario)

        // Operadores de null-coalescing
        string? str = null;
        string result = str ?? "Valor por defecto";  // result = "Valor por defecto"

        // Operador condicional ternario
        int z = 10;
        string mensaje = (z > 5) ? "Mayor que 5" : "Menor o igual a 5";

        // Ejemplo de uso
        EjemploCSharp();
    }

    static void EjemploCSharp()
    {
        int numero = 10;
        Console.WriteLine($"Número inicial: {numero}");
        
        numero += 5;
        Console.WriteLine($"Después de suma: {numero}");
        
        numero *= 2;
        Console.WriteLine($"Después de multiplicación: {numero}");
        
        numero %= 7;
        Console.WriteLine($"Después de módulo: {numero}");
    }
}
