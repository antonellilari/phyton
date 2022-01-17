a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))
c = int(input("terceiro valor: "))

if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c

print(f"Menor = {menor}")