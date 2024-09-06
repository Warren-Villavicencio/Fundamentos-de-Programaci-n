<?php

// Operadores de cálculo en PHP

// Suma (+)
$a = 5 + 3;  // $a = 8

// Resta (-)
$b = 10 - 4;  // $b = 6

// Multiplicación (*)
$c = 3 * 4;  // $c = 12

// División (/)
$d = 15 / 3;  // $d = 5

// Módulo (%)
$e = 17 % 3;  // $e = 2 (resto de la división)

// Exponenciación (**)
$f = 2 ** 3;  // $f = 8

// Operadores de asignación en PHP

// Asignación simple (=)
$x = 10;

// Asignación con suma (+=)
$x += 5;  // Equivalente a: $x = $x + 5

// Asignación con resta (-=)
$x -= 3;  // Equivalente a: $x = $x - 3

// Asignación con multiplicación (*=)
$x *= 2;  // Equivalente a: $x = $x * 2

// Asignación con división (/=)
$x /= 4;  // Equivalente a: $x = $x / 4

// Asignación con módulo (%=)
$x %= 3;  // Equivalente a: $x = $x % 3

// Asignación con exponenciación (**=)
$x **= 2;  // Equivalente a: $x = $x ** 2

// Operadores de concatenación
$str1 = "Hola ";
$str2 = "mundo";
$str3 = $str1 . $str2;  // $str3 = "Hola mundo"
$str1 .= $str2;  // $str1 = "Hola mundo"

// Operadores de incremento/decremento
$i = 5;
$i++;  // $i = 6
$j = 5;
$j--;  // $j = 4

// Ejemplo de uso
function ejemploPHP() {
    $numero = 10;
    echo "Número inicial: $numero\n";
    
    $numero += 5;
    echo "Después de suma: $numero\n";
    
    $numero *= 2;
    echo "Después de multiplicación: $numero\n";
    
    $numero %= 7;
    echo "Después de módulo: $numero\n";
}

ejemploPHP();
?>
