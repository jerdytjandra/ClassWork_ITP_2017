import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36,49]

numx   = [1,3,5,7,9]

numy   = [2,4,6,8,10]

plt.plot(squares,marker='o')
#plt.plot(numx,numy,marker = '*')

plt.title("series of numbers")
plt.xlabel("x coordinates")
plt.ylabel("y coordinates")

#plt.legend(["squares","numx and numy"])
plt.show()
