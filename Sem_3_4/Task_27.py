# Строка содержит набор чисел. Показать большее и меньшее число.
# Символ-разделитель - пробел

def min_and_max(str):
    list1 = str.split(' ')
    # print(list1)
    min = int(list1[0])
    max = int(list1[0])
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        if list1[i] < min:
            min = list1[i]
        if list1[i] > max:
            max = list1[i]
    return min, max
    # print(f'min: {min}, max: {max}')

a = input('enter anything: ')
print(min_and_max(a))