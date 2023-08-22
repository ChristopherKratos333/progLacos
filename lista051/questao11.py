'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de b elevado a e. (Sem usar Math.pow();)
'''

b = float(input("Informe a base da potência: "))
e = float(input("Informe o expoente da potência: "))

cont = 1
acum = 1
while cont <= e:
    acum = acum * b
    cont = cont + 1
print(f"{b:.0f} elevado à {e:.0f} = {acum:.0f}")