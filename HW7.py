'''
Завдання 1.
Написати рекурсивну функцію знаходження ступеня числа.
'''

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))

#power  (2,3) ->2 *power (2,2)=>8
#power  (2,2) ->2 *power (2,1)=>4
#power (2,1)->1


'''
Завдання 2.
Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
Проілюструйте роботу функції прикладом. (Протестувати)
'''
def print_stars(n):
    if n <= 0:
        return
    print('*', end='')
    print_stars(n-1)

N = int(input("Enter number of stars: "))
print_stars(N)
print ()
#Print * and call print_stars(N-1)
#.......
#Print * and call print_stars(3-1)=>2
#Print * and call print_stars(2-1)=>1
#Print * and call print_stars(1-1)=> will exit the loop


'''Завдання 3.
Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
Користувач вводить a та b. Проілюструйте роботу функції прикладом.
'''
def sum_range(a, b):
    if a > b:
        return 0
    return a + sum_range(a+1, b)

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(f"Sum of numbers from {a} to {b} = {sum_range(a, b)}")
#Imagine a=1 and b =3, the algos will be following
#sum_range (1,3)->1+sum_range(1+1,3) =>3
#sum_range (2,3)->1+sum_range(2+1,3) =>5
#sum_range (3,3)->1+sum_range(3+1,3) =>6
#sum_range (4,3)->1+sum_range(3+1,3) will exit the loop
'''
Завдання 4.
Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим
чином і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
'''

import random


def find_min_sum_position(arr, start=0):
    if start > len(arr) - 10:
        return -1

    current_sum = sum(arr[start:start + 10])
    next_sum_position = find_min_sum_position(arr, start + 1)

    if next_sum_position == -1:
        return start

    return start if current_sum < sum(arr[next_sum_position:next_sum_position + 10]) else next_sum_position


array = [random.randint(1, 100) for _ in range(100)]
position = find_min_sum_position(array)
print(f"Position from which a sequence of 10 numbers begins, the sum of which is the smallest: {position}")
