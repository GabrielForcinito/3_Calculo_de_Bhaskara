print("\nCálculo da Equação do 2º Grau (Bhaskara)")
 
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print("\nEquação Formada:")
print(f"{a}x² + {b}x + {c} = 0")

delta = ((b**2) - (4*a*c))
print("\nO resultado de Delta é =", delta)

rzd = (delta ** 0.5)
x1 = (-b + rzd) / (2*a)
x2 = (-b - rzd) / (2*a)

print("\nResultado das Raízes:")
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}\n")