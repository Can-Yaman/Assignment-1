question = "Please type a positive integer number: "
number = input(question).strip()
check_num = number.isnumeric()

while not check_num:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input(question).strip()
    
num = int(number)
power = len(number)
control_num = 0

for i in number: control_num += (int(i) ** power)
        
if control_num == num:
    print(f"{num} is an Armstrong number ")
else:
    print(f"{num} is not an Armstrong number ")
