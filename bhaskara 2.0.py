import math
print("\nVamos calcular a equação de segundo grau")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4*a*c

# Verifica se é equação do segundo grau
if a == 0:
    print("\nNão é equação do segundo grau!!!\n")

# Delta negativo
elif delta < 0:
    print("\nNão há raízes reais!!!\n")

# Delta igual a zero
elif delta == 0:
    x = -b / (2*a)
    print(f"\nRaiz única: x = {x:.2f}\n")

# Delta positivo
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"\nx1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}\n")
