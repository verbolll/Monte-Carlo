import matplotlib.pylab as plt

## old method
# numlist = []

# def getnum(M, lam, x0, c=0):
#     global numlist
#     xi = (lam * x0 + c) % M
#     if xi not in numlist:
#         numlist.append(xi)
#         print(numlist)
#     try:
#         newlist = numlist.copy()
#         return getnum(M, lam, xi, c)
#     except:
#         numlist = []
#         return sorted(newlist)

class LinearCongruentialGenerator:
    def __init__(self, m, a, seed, c=0):
        self.a = a
        self.c = c
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current