primes = []
count  = 0
for num in range(2,int(input("Enter a number to learn all prime numbers between 1 and entered number: "))) :
    for i in range (2,num) :
        if num % i == 0 : count += 1
    if count == 0 : primes.append(num)
    count = 0
print(primes)