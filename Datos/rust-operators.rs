fn main() {
    // Operadores de cálculo en Rust

    // Suma (+)
    let a = 5 + 3;  // a = 8

    // Resta (-)
    let b = 10 - 4;  // b = 6

    // Multiplicación (*)
    let c = 3 * 4;  // c = 12

    // División (/)
    let d = 15.0 / 3.0;  // d = 5.0

    // Módulo (%)
    let e = 17 % 3;  // e = 2 (resto de la división)

    // Operadores de asignación en Rust

    // Asignación simple (=)
    let mut x = 10;

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
    let mut y = 5;  // 101 en binario
    y <<= 1;    // Desplazamiento a la izquierda, y = 10 (1010 en binario)
    y >>= 1;    // Desplazamiento a la derecha, y = 5 (101 en binario)
    y &= 3;     // AND bit a bit, y = 1 (001 en binario)
    y |= 4;     // OR bit a bit, y = 5 (101 en binario)
    y ^= 1;     // XOR bit a bit, y = 4 (100 en binario)

    // Operadores de comparación
    let z = 10;
    println!("{}", x == z);  // false (igualdad)
    println!("{}", x != z);  // true (desigualdad)
    println!("{}", x > z);   // false (mayor que)
    println!("{}", x < z);   // true (menor que)
    println!("{}", x >= z);  // false (mayor o igual que)
    println!("{}", x <= z);  // true (menor o igual que)

    // Operadores lógicos
    let condicion1 = true;
    let condicion2 = false;
    println!("{}", condicion1 && condicion2);  // AND lógico
    println!("{}", condicion1 || condicion2);  // OR lógico
    println!("{}", !condicion1);               // NOT lógico

    // Operador de rango
    let rango = 1..=5;  // Rango inclusivo (incluye 5)
    let rango_exclusivo = 1..5;  // Rango exclusivo (excluye 5)

    // Ejemplo de uso
    ejemplo_rust();
}

fn ejemplo_rust() {
    let mut numero = 10;
    println!("Número inicial: {}", numero);
    
    numero += 5;
    println!("Después de suma: {}", numero);
    
    numero *= 2;
    println!("Después de multiplicación: {}", numero);
    
    numero %= 7;
    println!("Después de módulo: {}", numero);
}
