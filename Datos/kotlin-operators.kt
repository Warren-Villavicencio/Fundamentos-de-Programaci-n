// Operadores de cálculo básicos
val a = 10
val b = 3

val suma = a + b
val resta = a - b
val multiplicacion = a * b
val division = a / b
val modulo = a % b

// Operadores de asignación
var x = 5 // Asignación simple
x += 3 // x = x + 3
x -= 2 // x = x - 2
x *= 4 // x = x * 4
x /= 2 // x = x / 2
x %= 3 // x = x % 3

// Operadores de comparación y lógicos
val igualdad = a == b
val desigualdad = a != b
val mayorQue = a > b
val menorQue = a < b
val mayorIgual = a >= b
val menorIgual = a <= b

val and = true && false
val or = true || false
val not = !true

// Operadores específicos de Kotlin
// Operador de rango
val rango = 1..10
// Operador in
val enRango = 5 in rango

// Operador Elvis
val nullable: String? = null
val resultado = nullable ?: "Valor por defecto"

// Operador de llamada segura
val longitud = nullable?.length

// Operador de aserción no nula
val noNulo = nullable!!
