year = int(input("Input a 4-digit year: "))
leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:  leap = True
    else: leap = True
        
(lambda x: print(f"{year} is a leap year") if x else print(f"{year} is not a leap year"))(leap)