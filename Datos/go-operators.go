// Operadores de cálculo básicos
a := 10
b := 3

suma := a + b
resta := a - b
multiplicacion := a * b
division := a / b
modulo := a % b

// Operadores de asignación
x := 5 // Asignación simple
x += 3 // x = x + 3
x -= 2 // x = x - 2
x *= 4 // x = x * 4
x /= 2 // x = x / 2
x %= 3 // x = x % 3

// Operadores de comparación y lógicos
igualdad := a == b
desigualdad := a != b
mayorQue := a > b
menorQue := a < b
mayorIgual := a >= b
menorIgual := a <= b

and := true && false
or := true || false
not := !true

// Operadores específicos de Go
// Operador de canal bidireccional
ch := make(chan int)
// Enviar valor al canal
ch <- 42
// Recibir valor del canal
valor := <-ch

// Operador de puntero y dirección
var p *int = &a
