# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
x = int(input("x: "))
y = int(input("y: "))


def coordinates(x, y):
    if (x > 0 and y > 0):
        print("Точка находится в 1 четверти")
    if (x < 0 and y > 0):
        print("Точка находится во 2 четверти")
    if (x < 0 and y < 0):
        print("Точка находится в 3 четверти")
    if (x > 0 and y < 0):
        print("Точка находится в 4 четверти")
coordinates (x,y)

