eixos1 = input().split()
eixos2 = input().split()

x1 = float(eixos1[0])
y1 = float(eixos1[1])

x2 = float(eixos2[0])
y2 = float(eixos2[1])

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"{distancia:.4f}")