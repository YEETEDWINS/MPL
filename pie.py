import matplotlib.pyplot as mpl

colors = ["r", "g", "b", "c", "m", "w", "y", "k"]
colorsChance = [6, 12, 90, 31, 92, 332, 49, 3]

mpl.pie(colorsChance, labels = None, colors = colors, startangle = 0, shadow = True)
mpl.title("F3 Chart")
mpl.show()

