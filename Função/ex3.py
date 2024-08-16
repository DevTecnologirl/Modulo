valor = input()

def cedulas(valor):
    print(valor)
    notas = valor/100
    print("%d nota(s) de R$ 100,00" %notas)
    valor = valor%100

    notas = valor/50
    print("%d nota(s) de R$ 50,00" %notas)
    valor = valor%50

    notas = valor/20
    print("%d nota(s) de R$ 20,00" %notas)
    valor = valor%20

    notas = valor/10
    print("%d nota(s) de R$ 10,00" %notas)
    valor = valor%10

    notas = valor/5
    print("%d nota(s) de R$ 5,00" %notas)
    valor = valor%5

    notas = valor/2
    print("%d nota(s) de R$ 2,00" %notas)
    valor = valor%2

    print("%d nota(s) de R$ 1,00" %valor)

cedulas(int(valor))