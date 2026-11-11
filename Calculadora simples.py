while True:
    print("\nCalculadora simples")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo...")
        break

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida.")
        continue

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números válidos.")
        continue

    if opcao == "1":
        resultado = numero1 + numero2
        operacao = "+"
    elif opcao == "2":
        resultado = numero1 - numero2
        operacao = "-"
    elif opcao == "3":
        resultado = numero1 * numero2
        operacao = "*"
    elif opcao == "4":
        if numero2 == 0:
            print("Erro: divisão por zero.")
            continue
        resultado = numero1 / numero2
        operacao = "/"

    print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")

    continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
    if continuar != "s":
        print("Saindo...")
        break
    