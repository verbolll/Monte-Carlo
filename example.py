import numpy as np
def exa(num):
    i = 0
    for i1 in range(num):
        random_value = np.random.uniform(0, 1, 6)

        sigmaG = 0.1
        muG = 0.3

        x1 = (muG + sigmaG*np.sqrt(-2*np.log(random_value[0]))*np.cos(2*np.pi*random_value[1]))
        # x2 = (muG + sigmaG*np.sqrt(-2*np.log(random_value[0]))*np.sin(2*np.pi*random_value[1]))


        sigmaM1 = 62.2
        muM1 = 414.8

        x11 = (muM1 + sigmaM1*np.sqrt(-2*np.log(random_value[2]))*np.cos(2*np.pi*random_value[3]))
        # x22 = (muM1 + sigmaM1*np.sqrt(-2*np.log(random_value[2]))*np.sin(2*np.pi*random_value[3]))


        sigmaM2 = 62.2*((1-0.8**2)**0.5)
        muM2 = 622.2-0.8*414.8+0.8*x11


        x111 = (muM2 + sigmaM2*np.sqrt(-2*np.log(random_value[4]))*np.cos(2*np.pi*random_value[5]))
        # x222 = (muM2 + sigmaM2*np.sqrt(-2*np.log(random_value[4]))*np.sin(2*np.pi*random_value[5]))

        w = 453.6
        h = 4.57
        l = 6.1

        g1 = 4*x11 - x1*w*h
        g2 = 4*x11 +2*x111 - x1*w*h - 0.5*w*l
        g3 = 2*x11 +2*x111 -0.5*w*l
        g4 = 2*x11 +4*x111 -x1*w*h - 0.5*w*l

        if g1 > 0 and g2 > 0 and g3 > 0 and g4 > 0:
            i = i + 1
            # print(i)


    return ((num-i) / num)

# exa(500)