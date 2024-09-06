// Operadores de cálculo básicos
let a: number = 10;
let b: number = 3;

let suma: number = a + b;
let resta: number = a - b;
let multiplicacion: number = a * b;
let division: number = a / b;
let modulo: number = a % b;

// Operadores de asignación
let x: number = 5; // Asignación simple
x += 3; // x = x + 3
x -= 2; // x = x - 2
x *= 4; // x = x * 4
x /= 2; // x = x / 2
x %= 3; // x = x % 3

// Operadores de comparación y lógicos
let igualdad: boolean = a === b; // Igualdad estricta
let desigualdad: boolean = a !== b; // Desigualdad estricta
let mayorQue: boolean = a > b;
let menorQue: boolean = a < b;
let mayorIgual: boolean = a >= b;
let menorIgual: boolean = a <= b;

let and: boolean = true && false;
let or: boolean = true || false;
let not: boolean = !true;

// Operadores específicos de TypeScript
// Operador de aserción de tipo
let valor: any = "Hola";
let longitud: number = (valor as string).length;

// Operador de unión de tipos
let unionTipo: string | number = "Texto";
unionTipo = 42;

// Operador de encadenamiento opcional
type Persona = { nombre?: { apellido?: string } };
let persona: Persona = {};
let apellido = persona.nombre?.apellido;

// Operador de coalescencia nula
let nulo: string | null = null;
let resultado: string = nulo ?? "Valor por defecto";
