def copy():

    random = open("philosophers.txt", "r")
    x=random.read()
    random.close()
    z=open("Philosophers.txt.ne", "w")
    z.write(x)
    z.close()

copy()
