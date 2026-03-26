import matplotlib.pyplot as plt
# size=[15,30,45,10]
# labels=["A","B","C","D"]
# colors=["gold","yellowgreen","lightcoral","lightskyblue"]
# explode=(0,0.1,0,0)
# plt.pie(size,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True,startangle=140)
# plt.title("piechart")
# plt.axis('equal')
# plt.show()

import numpy as np
x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
x,y=np.meshgrid(x,y)
z=np.sin(np.sort(x**2+y**2))
plt.contour(x,y,z,levels=10,cmap="viridis")
plt.title("contour plot")
plt.colorbar()
plt.show()