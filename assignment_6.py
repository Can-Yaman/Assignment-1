given_num = int(input("Enter a number to learn all prime numbers between 1 and entered number: "))
prime_numbers = []
for i in range(2, given_num):
    divider_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    num = i
    check = False
    if num in divider_num:
        if num in [2, 3, 5, 7, 11]: pass
        else: check = True
    else:
        for j in divider_num: check = check or (not (num % j))
            
    if not check: prime_numbers.append(num)
print(f"This is the list of prime numbers between 1 and {given_num}:")
print(prime_numbers)