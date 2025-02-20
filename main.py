def calcular(x, y, operacao):
    operacoes = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y if y != 0 else "Erro! Divisão por zero."
    }
    return operacoes.get(operacao, lambda x, y: "Operação inválida!")(x, y)

def calculadora():
    print("Selecione uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calcular(num1, num2, escolha)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Você deve digitar números válidos.")

if __name__ == "__main__":
    calculadora() 
