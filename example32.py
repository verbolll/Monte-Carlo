import numpy as np
def exa(num):
    i = 0
    for i1 in range(num):
        random_value = np.random.uniform(0, 1, 6)

        mue = 72000
        sigmae = mue * 0.06
        

        x1 = (mue + sigmae*np.sqrt(-2*np.log(random_value[0]))*np.cos(2*np.pi*random_value[1]))
        # x2 = (muG + sigmaG*np.sqrt(-2*np.log(random_value[0]))*np.sin(2*np.pi*random_value[1]))

        mup = 0.4
        sigmap = mup * 0.15

        x11 = (mup + sigmap*np.sqrt(-2*np.log(random_value[2]))*np.cos(2*np.pi*random_value[3]))
        # x22 = (muM1 + sigmaM1*np.sqrt(-2*np.log(random_value[2]))*np.sin(2*np.pi*random_value[3]))


        g= 0.00351*x1 -333.333*x11
        
        if g > 0:
            i = i + 1
            # print(i)


    print((num-i) / num)

exa(100000)