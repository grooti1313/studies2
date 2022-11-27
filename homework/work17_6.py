n = list(map(int,input('Введите количество чисел в последовательности через пробел: ').split()))
number = int(input("Введите любое число: "))
n.append(number)

for i in range(1, len(n)):
    x = n[i]
    idx = i
    while idx > 0 and n[idx-1] > x:
        n[idx] = n[idx-1]
        idx -= 1
    n[idx] = x
    if x == number and idx+2 <= len(n) and x != 0:
        print('Индекс числа', idx+1, 'больше индекса числа', idx, "и меньше или равно индексу числа", idx+2)
    if idx+2 > len(n):
        print('Индекс числа', idx+1, 'больше индекса числа', idx, "и меньше или равно индексу числа нет (это максимальное число)")
    if x == 0:
        print("Числа меньше введенного индекса нет")
print(n)