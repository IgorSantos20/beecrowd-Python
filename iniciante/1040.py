notas = input().split()

notas_float = list(map(float, notas))

nota1 = notas_float[0]
nota2 = notas_float[1]
nota3 = notas_float[2]
nota4 = notas_float[3]

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) /10

print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (nota_exame + media) / 2
    if media >=5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")
