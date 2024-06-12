import numpy as np

def fx(sigma, mu):
    random_value = np.random.uniform(0, 1, 2)
    x1 = (mu + sigma*np.sqrt(-2*np.log(random_value[0]))*np.cos(2*np.pi*random_value[1]))
    return x1

def exa(num):
    i = 0
    for i1 in range(num):

        q = fx(0.0333, 1.15)
        l = fx(0.6, 60)
        b = fx(0.12, 4)
        h = fx(0.03, 1)
        f = fx(300, 3600)

        g1 = f - ((3*q*l*l) / (b*h*h))

        if g1 > 0:
            i = i + 1


    return ((num-i) / num)

# 中心点法 0.0962
# 验算点法 0.184