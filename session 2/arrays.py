import numpy as np
arr1d = np.array([1,2,3,4,5,])
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr1d)
print(arr2d)
arr = np.array([1,2,3,4,5,6])
print(arr[2])
print(arr[1:4])

x = [1,2,3]
y = [4,5,6]

print(x+y)

sum1  = np.array([1,2,3])
sum2 = np.array([4,5,6])
print(sum1 + sum2)
print(sum1 * sum2)



resizeArr = np.array([1,2,3,4,5,6])
print(resizeArr.reshape(2,3))

statArr = np.array([1,2,3,4,5,6])
mean = np.mean(statArr)
max_val =np.sum(statArr)
total = np.sum(statArr)




randArr =np.random.randint(25, size=(5))
meanArr = np.mean(randArr)
maxArr = np.max(randArr)
minArr = np.min(randArr)
sumArr = np.sum(randArr)
sortArr = np.sort(randArr)
shuffleArr = np.random.shuffle(randArr)
squareArr = randArr * randArr
sqrtArr = np.sqrt(randArr)
print(meanArr, maxArr, minArr, sumArr, sortArr, shuffleArr, squareArr, sqrtArr, randArr, sep = " ")    
    



