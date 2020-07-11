x, y = 1, 0
fibonaccies = []
while x <= 55:
    fibonaccies.append(x)
    x, y = x+y, x
print("These are  Fibonacci numbers from 1 to 55:", fibonaccies, sep = "\n")