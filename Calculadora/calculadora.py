def calcular(primeiro_num, operacao, segundo_num):
    if operacao == '+':
        return primeiro_num + segundo_num
    elif operacao == '-':
        return primeiro_num - segundo_num
    elif operacao == '*':
        return primeiro_num * segundo_num
    elif operacao == '/':
        if segundo_num == 0:
            print("Erro: Divisão por zero!")
            return None
        return primeiro_num / segundo_num
    else:
        print("Operação inválida!")
        return None


while True:
    try:
        primeiro_num = float(input("Digite o primeiro número: \n"))
        operacao = input(
            "Digite a operação que você deseja fazer: [+]Soma, [-]Subtração, [*]Multiplicação, [/]Divisão: \n")
        segundo_num = float(input("Digite o segundo número: \n"))

        resultado = calcular(primeiro_num, operacao, segundo_num)

        if resultado is not None:
            print(f"O resultado é: {resultado}")

    except ValueError:
        erro_repetir = input(
            "O valor digitado é inválido! Deseja repetir? Tecle [s] para 'sim' e qualquer tecla para 'não' ").lower()
        if erro_repetir != 's':
            print("Fim do programa.")
            break

    fim = input('Pressione [r] para repetir ou [s] para sair ').lower()

    if fim != 'r':
        print("Fim do programa.")
        break
