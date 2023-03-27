#### exercício de averiguar o maior número

def maior(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

function = maior(num1, num2)

print(function)




#### exercício de múltiplos 2

def ftrue(num3, num4):
    if num3 % num4 == 0:
        return True 
    else:
        return False

num3 = int(input("Insira o primeiro número: "))
num4 = int(input("Insira o segundo número: "))

cal = ftrue(num3, num4)
print(cal)






##### área do quadrado 

def quadrado(num5):
    return num5**2

num5 = int(input("Digite o lado do quadrado: "))
calculo = quadrado(num1)

print(calculo)