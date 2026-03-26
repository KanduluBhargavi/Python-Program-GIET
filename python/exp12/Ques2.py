import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[5,7,8,6,7]
# plt.scatter(x,y,color="b",label="scatter_plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()

categories=["A","B","C","D"]
values=[3,7,8,5]
plt.bar(categories,values,color="y",label="Bardata")
plt.title("barplot")
plt.xlabel("categories")
plt.ylabel("values")
plt.legend()
plt.show()
