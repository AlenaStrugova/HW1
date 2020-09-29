import math
print("Введите коэффициенты для уравнения")
print("x^2 + bx + c = 0:")
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * c
print("Дискриминант = ", discr)
if discr == b ** 2:
    x1 = -b
    x2 = c/x1
    print(x1, x2)
elif discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2)
    x2 = (-b - math.sqrt(discr)) / (2)
    if abs(x1) > 1e10 * abs(x2):
        x2 = c/x1
    print("x1 =", x1, "x2 = ", x2)
elif discr == 0:
    x = -b / (2)
    print("x = ", x)
else:
    x1 = (-b + discr ** 0.5) / (2)
    x2 = (-b - discr ** 0.5) / (2)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
