valores = input().split()
valores_inteiros = list(map(float, valores))

reta1 = valores_inteiros[0]
reta2 = valores_inteiros[1]
reta3 = valores_inteiros[2]

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    perimetro_triangulo = reta1 + reta2 + reta3
    print(f"Perimetro = {perimetro_triangulo:.1f}")
else:
    area_trapezio = ((reta1 + reta2) * reta3) / 2
    print(f"Area = {area_trapezio:.1f}")