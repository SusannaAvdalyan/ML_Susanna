import matplotlib.pyplot as plt

categories = ['Cat A', 'Cat B', 'Cat C ', 'Cat D', 'Cat E']
percentages = [25, 30, 15, 30, 36]

explode = [0, 0.1, 0, 0, 0.2]

colors = ['red', 'blue', 'green', 'orange', 'yellow']

plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)

plt.title('Percentage Distribution')

plt.legend(categories)

plt.show()
