import numpy as np
import matplotlib.pyplot as plt

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
distanceKm = [57.9, 180.2, 149.6, 227.9, 777.3, 1400, 2900, 4500]

for i in range (len(distanceKm)):
    AU =  distanceKm[i]/149.6
    i+=1
    print(AU)

plt.plot(planets, distanceKm, marker='o', linestyle = '--', color = 'aqua')
plt.xlabel("Planets")
plt.ylabel("Distance")
plt.title("Planets and disctances")
plt.show()


print('------------------')

maxVal = np.max(distanceKm)
minVal = np.min(distanceKm)
meanVal = np.mean(distanceKm)
print('Max: ', maxVal)
print('Min: ', minVal)
print('Mean: ', meanVal)

