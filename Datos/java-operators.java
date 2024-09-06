public class OperadoresJava {
    public static void main(String[] args) {
        // Operadores de cálculo en Java

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

        // Incremento (++)
        int f = 5;
        f++;  // f = 6

        // Decremento (--)
        int g = 5;
        g--;  // g = 4

        // Operadores de asignación en Java

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

        // Ejemplo de uso
        ejemploJava();
    }

    public static void ejemploJava() {
        int numero = 10;
        System.out.println("Número inicial: " + numero);
        
        numero += 5;
        System.out.println("Después de suma: " + numero);
        
        numero *= 2;
        System.out.println("Después de multiplicación: " + numero);
        
        numero %= 7;
        System.out.println("Después de módulo: " + numero);
    }
}
