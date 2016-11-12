"""
Напишите функцию, разлагающую данное число на простые множители. Результатом
работы программы должен быть список, в котором каждому простому множителю p и
его степени k соответствует пара (p, k) (вложенный список). Например, число 12 должно
быть разложено так: [[2, 2], [3, 1]].
"""


def multiplies(n):
    if n == 1:
        return [[1, 1]]

    result = []

    for multiplier in range(2, n + 1):
        power = 0
        while n % multiplier == 0:
            n /= multiplier
            power += 1

        if power > 0:
            result.append([multiplier, power])

    return result


for i in range(2, 20):
    print(str(i) + ": " + str(multiplies(i)))
