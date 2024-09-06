// Operadores de cálculo en JavaScript

// Suma (+)
let a = 5 + 3;  // a = 8

// Resta (-)
let b = 10 - 4;  // b = 6

// Multiplicación (*)
let c = 3 * 4;  // c = 12

// División (/)
let d = 15 / 3;  // d = 5

// Módulo (%)
let e = 17 % 3;  // e = 2 (resto de la división)

// Exponenciación (**)
let f = 2 ** 3;  // f = 8

// Incremento (++)
let g = 5;
g++;  // g = 6

// Decremento (--)
let h = 5;
h--;  // h = 4

// Operadores de asignación en JavaScript

// Asignación simple (=)
let x = 10;

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

// Asignación con exponenciación (**=)
x **= 2;  // Equivalente a: x = x ** 2

// Ejemplo de uso
function ejemploJavaScript() {
    let numero = 10;
    console.log(`Número inicial: ${numero}`);
    
    numero += 5;
    console.log(`Después de suma: ${numero}`);
    
    numero *= 2;
    console.log(`Después de multiplicación: ${numero}`);
    
    numero %= 7;
    console.log(`Después de módulo: ${numero}`);
}

ejemploJavaScript();
