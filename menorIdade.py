idade = int(input("Digite sua idade: "))
menorIdade = True

if idade < 18:
    if menorIdade:
        print("Menor de idade porém está acompanhado.")
    else:
        print("Maior idade porém não está acompanhado.")
else:
        print("Maior idade")