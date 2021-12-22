# Task 4

number = input("Введите целое положительное число: ")
number = int(number)
bignum = 0
while number > 0:
    lastnum = number % 10
    number = number // 10
    if lastnum > bignum:
        bignum = lastnum
print(f"Самая большая цифра в веденном числе = {bignum}")