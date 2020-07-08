age =  input("If you are a cigarette addict older than 75 years old. Answer yes or no: ").lower() == "yes"

chronic  = input("If you have a severe chronic disease. Answer yes or no: ").lower() == "yes"

immune  = input("If your immune system is too weak. Answer yes or no: ").lower() == "yes"

death_risk = age and (chronic or  immune)

if death_risk:
    print("You are in risky group")
else:
    print("You are not in risky group")