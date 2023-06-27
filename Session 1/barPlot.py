import matplotlib.pyplot as plt

products = ['Pr1', 'Pr2', 'Pr3', 'Pr4']

sales = [350, 480, 290, 520]

plt.bar(products, sales, color = ['red', 'blue', 'green', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()

