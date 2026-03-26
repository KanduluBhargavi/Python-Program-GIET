import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,25,30]

plt.title("simple line plot")
plt.plot(x,y,linestyle="--",color="r",marker="o",label="Dataline")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.legend()
plt.grid()
plt.show()
