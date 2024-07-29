import matplotlib.pyplot as mpl

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]

mpl.scatter(x, y, label="Scatter Plot", color="red", marker="*", s=30)

mpl.xlabel("Unsquared")
mpl.ylabel("Squared")
mpl.title("x²")

mpl.show()