import matplotlib.pyplot as plt


def f(s):
    a = ""
    for i in range(len(s)):
        if s[i] == "-":
            continue
        a += s[i]
    return int(a)
def minn(v):
    minn = pow(10,5)
    for i in v:
        minn = min(i,minn)
    return minn
def maxx(v):
    maxx = 0
    for i in v:
        maxx = max(i, maxx)
    return maxx
        


cb  = [230, 285, 320, 225, 310, 270, 200, 305, 240]
sc = [5023, 6201, 7542, 4908, 7020, 5832, 4312, 6789, 5231]
data = [1, 2, 3, 4, 5, 6,7, 8, 9]
dataMin = pow(10,5)
dataMax = 0

plt.style.use('_mpl-gallery')

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(cb,sc, data)
ax.set_xlim(minn(cb),maxx(cb))
ax.set_ylim(minn(sc),maxx(sc))
ax.set_zlim(minn(data),maxx(data))
ax.set_xlabel("calories B")
ax.set_ylabel("step")
ax.set_zlabel("data")
plt.show()
