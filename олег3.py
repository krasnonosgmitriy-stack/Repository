import matplotlib.pyplot as plt
from олег2 import create_x, create_y
x = create_x(-50, 50,100)
y = create_y(-50, 50,100)

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, y, label='linear') # Plot some data on the (implicit) Axes.
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.grid()
plt.show()



#plt.figure(figsize=(5, 2.7), layout='constrained')
#plt.plot(x, y, label='linear')  # Plot some data on the (implicit) Axes.
#plt.plot(x, y**2, label='quadratic')  # etc.
#plt.plot(x, y**3, label='cubic')
#plt.xlabel('x label')
#plt.ylabel('y label')
#plt.title("Simple Plot")
#plt.legend()
#plt.show()