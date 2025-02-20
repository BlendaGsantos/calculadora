def calcular(x, y, operacao):
    operacoes = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y if y != 0 else "Erro! Divisão por zero."
    }
    return operacoes.get(str(operacao), lambda x, y: "Operação inválida!")(x, y)

def calculadora():
    print("Selecione uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    try:
        escolha = int(input("Digite o número da operação (1/2/3/4): "))
        
        if 1 <= escolha <= 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = calcular(num1, num2, escolha)
            print(f"Resultado: {resultado}")
        else:
            print("Erro: Você deve digitar um número entre 1 e 4.")
    
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro para a operação.")

if __name__ == "__main__":
    calculadora()