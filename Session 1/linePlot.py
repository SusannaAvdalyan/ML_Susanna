import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016, 2018, 2020]
population = [8.5, 9.1, 9.8, 10.5, 12.3, 6.5]

plt.plot(years, population, marker = 'o', linestyle = '--', color = 'green')
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Population Growth Over Years')
plt.show()
