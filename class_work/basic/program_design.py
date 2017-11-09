#Good program design:
# -functions -> how to design
# -Objects   -> how to design

#Foundations:
# -control statements(if)
# -loops
# data structures (int, string, list, dictionary)
numbers = [5,75,15,20,8,9,10,23,45,50]

def max_number():
    max = 0
    for number in numbers:
        if number > max:
            max = number
    print(max)

max_number()
