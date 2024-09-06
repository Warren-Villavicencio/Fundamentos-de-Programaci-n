import Foundation

// Operadores de cálculo en Swift

// Suma (+)
let a = 5 + 3  // a = 8

// Resta (-)
let b = 10 - 4  // b = 6

// Multiplicación (*)
let c = 3 * 4  // c = 12

// División (/)
let d = 15.0 / 3.0  // d = 5.0

// Módulo (%)
let e = 17 % 3  // e = 2 (resto de la división)

// Operadores de asignación en Swift

// Asignación simple (=)
var x = 10

// Asignación con suma (+=)
x += 5  // Equivalente a: x = x + 5

// Asignación con resta (-=)
x -= 3  // Equivalente a: x = x - 3

// Asignación con multiplicación (*=)
x *= 2  // Equivalente a: x = x * 2

// Asignación con división (/=)
x /= 4  // Equivalente a: x = x / 4

// Asignación con módulo (%=)
x %= 3  // Equivalente a: x = x % 3

// Operadores de comparación
let y = 5
let z = 10
print(y == z)  // false (igualdad)
print(y != z)  // true (desigualdad)
print(y > z)   // false (mayor que)
print(y < z)   // true (menor que)
print(y >= z)  // false (mayor o igual que)
print(y <= z)  // true (menor o igual que)

// Operadores lógicos
let condicion1 = true
let condicion2 = false
print(condicion1 && condicion2)  // AND lógico
print(condicion1 || condicion2)  // OR lógico
print(!condicion1)               // NOT lógico

// Operador de rango
let rango = 1...5  // Rango cerrado (incluye 5)
let rangoAbierto = 1..<5  // Rango semi-abierto (excluye 5)

// Operador nil-coalescing
let opcional: String? = nil
let valorPorDefecto = opcional ?? "Valor por defecto"

// Ejemplo de uso
func ejemploSwift() {
    var numero = 10
    print("Número inicial: \(numero)")
    
    numero += 5
    print("Después de suma: \(numero)")
    
    numero *= 2
    print("Después de multiplicación: \(numero)")
    
    numero %= 7
    print("Después de módulo: \(numero)")
}

ejemploSwift()
