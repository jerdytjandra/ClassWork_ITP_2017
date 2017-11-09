while True:
    age = int(input("Enter your age:"))
    if age < 3:
        print("The ticket is free.\n")
    elif 3<=age<=12:
        print("The ticket is $10.\n")
    elif age>12:
        print("The ticket is $15.\n")
