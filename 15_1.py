import matplotlib.pyplot as plt

x_vals = [1,2,3,4,5]
y_vals = [x**3 for x in x_vals]

# plt.scatter(x_vals, y_vals,c='red',edgecolors='none',s=40)
plt.scatter(x_vals, y_vals,
            c=y_vals,cmap=plt.cm.Blues,
            edgecolors='none',s=40)

plt.title("cubed numbers",fontsize=14)
plt.xlabel("value",fontsize=14)
plt.ylabel("cubes of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.axis([-0.1,5.1,0,5.1**3])

plt.show()