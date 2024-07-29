# Stackplots are like pie charts, but in stacks.

import matplotlib.pyplot as mpl

# Hours in a day
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Activities
gaming = [0, 0, 0, 0, 2, 5, 4, 5, 6, 6]
homework = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
eating = [10, 1, 1, 1, 1, 0, 1, 1, 1, 2]

# Stack plot
mpl.stackplot(hours, gaming, homework, eating, labels=['Gaming', 'Working', 'Eating'], colors=['#FF6347', '#4682B4', '#90EE90'])

# Adding legend, title, and labels
mpl.legend(loc='upper left')
mpl.title('Daily Activities')
mpl.xlabel('Hours')
mpl.ylabel('Activities')

# Display the plot
mpl.show()
