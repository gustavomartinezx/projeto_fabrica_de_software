def maior(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

function = maior(num1, num2)

print(function)