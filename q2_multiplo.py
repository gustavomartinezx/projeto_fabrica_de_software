def ftrue(num1, num2):
    if num1 % num2 == 0:
        return True 
    else:
        return False

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

cal = ftrue(num1, num2)
print(cal)