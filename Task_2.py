# Найти максимальное из пяти чисел

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))
def find_max (*args):
    tmp = -1
    for i in args:
        if (i > tmp):
            tmp=i
    return tmp
print(find_max(a,b,c,d,e))