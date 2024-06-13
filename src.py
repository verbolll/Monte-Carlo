from MonteCarlo import bignum
import matplotlib.pylab as plt
def draw(method, p, time):
    step_list = []
    x_list = []
    for i in range(time):
        x_list.append(i+2)
        if method == 'bernoulli':
            step_list.append(bignum.bernoulli(p, i+2))
        elif method == 'poisson':
            step_list.append(bignum.poisson(p, i+2))
    print(step_list)
    plt.plot(x_list, step_list, color='b')
    plt.plot([0, (i+1)], [p, p], color='red')
    plt.savefig('my_plot.png', dpi=300)
    plt.close()

