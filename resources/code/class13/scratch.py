import matplotlib.pyplot as plt
plt.figure(1)
#plt.subplot(1, 1, 1)
plt.subplot(211)
plt.plot([1, 2, 3], 'r--')

#plt.figure(2)
#plt.subplot(1, 2, 2)
plt.subplot(212)
plt.plot([3, 2, 1])

plt.show()
