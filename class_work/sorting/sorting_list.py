def myfactorial(x):
    if x==1: return 1
    else:
        y=x*myfactorial(x-1)
    return y
z= int(input('Input number:'))
print(myfactorial(z))

