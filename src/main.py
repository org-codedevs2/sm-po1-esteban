import sys

def sumar(a: float, b: float) -> float:
    return a + b

if __name__ == "__main__":
    # Lee los números pasados como argumentos o usa 10 y 20 por defecto
    num1 = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
    num2 = float(sys.argv[2]) if len(sys.argv) > 2 else 20.0

    resultado = sumar(num1, num2)
    print(f"➕ La suma de {num1} + {num2} es: {resultado}")