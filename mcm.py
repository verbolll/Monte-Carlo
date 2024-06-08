import matplotlib.pylab as plt

numlist = []

def getnum(M, lam, x0, c=0):
    global numlist
    xi = (lam * x0 + c) % M
    if xi not in numlist:
        numlist.append(xi)
        print(numlist)
    try:
        newlist = numlist.copy()
        return getnum(M, lam, xi, c)
    except:
        numlist = []
        return sorted(newlist)

# getnum(2**9, 5, 1)
# plt.plot(numlist)
# print(sorted(numlist))
# plt.show()