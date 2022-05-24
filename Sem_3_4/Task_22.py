# Найти сумму чисел списка стоящих на нечетной позиции

numbers = [2, 5, 7, 1, 8]
total = 0
for number in range(len(numbers)):
    if number % 2 != 0:
        total += numbers[number]
        print('index:', number, '=', numbers[number])
print('Sum:', total)
