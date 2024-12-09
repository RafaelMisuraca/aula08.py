import math

def area_cilindro(a, b, c, d):
  return a * b * c * (c + d)

raio = float(input("Digite aqui o raio: "))
altura = float(input("Digite a altura: "))

print(f"{area_cilindro(2, math.pi, raio, altura):.2f}")
