user_name = "can"

password = "victory2020"

visiter_name = input("Type your user name").lower()

check = visiter_name == user_name

if check:

    print(f"Hello, {visiter_name.title()}! The password is : {password}") 

else:

    print(f"Hello, {visiter_name.title()}! See you later.") 