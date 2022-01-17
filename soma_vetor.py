N = int(input("Quantos numeros voce vai digitar?"))

vet = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("digite um numero: "))

print()
print("VALORES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f} ", end="")

print()

soma = 0
for i in range(0, N):
    soma = soma + vet[i]

print(f"SOMA = {soma:.2f}")

media = soma / N
print(f"Media = {media:.2f}")

