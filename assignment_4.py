divider_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
num = int(input("Please input a number to check if it's a prime number or not: "))
result = False
if num in divider_num:
    if num in [2, 3, 5, 7, 11]:
        result = False
    else:
        result = True
else:
    for i in divider_num:
        result = result or (not (num % i))
        
print((not result) * f"{num} is a prime number" + result * f"{num} is not a prime number")
