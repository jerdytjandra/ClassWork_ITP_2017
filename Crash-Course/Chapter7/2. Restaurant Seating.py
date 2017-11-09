guests = int(input("How many people are in your dinner group?"))

if guests > 8:
    message1 = "Sorry, you will have to wait for a table."
    print(message1)
else:
    message2 = "The table is ready."
    print(message2)
