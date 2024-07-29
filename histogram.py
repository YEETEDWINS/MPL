import matplotlib.pyplot as mpl

ages = [25, 36, 95, 76, 45, 67, 53, 44, 52, 29, 1, 14]

levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

mpl.hist(ages, levels, rwidth="0.7")

mpl.xlabel("Age Interval")
mpl.ylabel("Frequency")
mpl.title("Histogram")
mpl.show()