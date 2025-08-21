# Calculadora simples em Python 🧮

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis: +, -, *, /")
    
    while True:
        operacao = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ").strip()
        if operacao.lower() == 'sair':
            print("Calculadora encerrada. Até logo!")
            break
        
        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    calculadora()
