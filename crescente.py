print("digite dois numeros: ")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("crescente!")
    else:
        print("decrescente!")

    print("digite outro dois numeros")
    x = int(input())
    y = int(input())