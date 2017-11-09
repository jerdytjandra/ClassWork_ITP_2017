import matplotlib.pyplot as plt

numx = list(range(1, 1001))
numy = [x**2 for x in numx]

plt.scatter(numx, numy, c=numy)
#plt.scatter(numx,numy,c='blue',cmap=plt.cm.Blues, edgecolors = 'none', s=40)

plt.axis([0, 1100, 0, 1100000])
plt.show()
