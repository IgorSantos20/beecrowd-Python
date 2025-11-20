salario = float(input())

percentual = 0
reajuste = 0
if salario >= 0 and salario <= 400.00:
    percentual = 15
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

elif salario >= 400.01 and salario <= 800.00:
    percentual = 12
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

elif salario >= 800.01 and salario <= 1200.00:
    percentual = 10
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

elif salario >= 1200.00 and salario <= 2000.00:
    percentual = 7
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

else:
    percentual = 4
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")