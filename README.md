# lab3
#1
n = int(input())

num = 2  

while num <= n:
    print(num)
    num += 2  

#2
n = int(input())
result = 1

while n > 0:
    result *= n
    n -= 1

print(result)

#3
while True:
    n = int(input())
    
    if n == 42:
        print()
        break

#4
b = input()

count = b.count('a')

print(count)

#5
n = input()

print(sum(int(digit) for digit in n if digit.isdigit()))

#6
N = int(input())

a, b = 0, 1

while N > 0:
    print(a, end=" ")
    a, b = b, a + b
    N -= 1

#7
N = input()

print(N[::-1])


#8
sum = 0

while True:
    a = input()

    if a == '.':
        break

    n = int(a)

    if n % 2 != 0:
        sum += n

print(sum)

#9
import random

n = random.randint(1, 100)

while True:
    a = int(input(" от 1 до 100: "))

    if a < n:
        print("Слишком мало")
    elif a > n:
        print("Слишком много")
    else:
        print(f"Правильно! {n}.")
        break

 #10
a = input()

n = a.replace(" ", "").lower()

if n == n[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

#11
X = float(input(" X: "))

Y = int(input(" Y: "))

result = 1

while Y > 0:
    result *= X
    Y -= 1

print(result)

#12
N = int(input())

if N < 2:
    print("no prostyx")
else:
    print("от 1 до", N, ":")
    number = 2

    while number <= N:
        isPrime = True
        current = 2

        while current < number:
            if number % current == 0:
                isPrime = False
                break
            current += 1

        if isPrime:
            print(number)

        number += 1

#13
n = input()

y = ""

for i in range(len(n) - 1, -1, -1):
    y += n[i]

print(y)

#14
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

X = int(input())

while not isPrime(X):
    X += 1

print(X)

#15
user = input("Введите строку: ")

N = int(input("Введите сдвиг N: "))

encrypted = ""

for char in user:
    if char.isalpha():
        shifted = chr(ord(char) + N)
        if char.isupper() and shifted > 'Z':
            shifted = chr(ord(shifted) - 26)
        if char.islower() and shifted > 'z':
            shifted = chr(ord(shifted) - 26)
        encrypted += shifted
    else:
        encrypted += char

print("Зашифрованная строка:",encrypted)
