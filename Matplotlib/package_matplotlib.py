import matplotlib.pyplot as plt
import numpy as np
def plot():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.show()

def plot1():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    pt1 = plt.plot(X, C)
    pt2 = plt.plot(X, S)
    print(pt1, pt2)

    plt.show()

def plot2():
    years = [x for x in range(1950, 2011, 10)]
    gdp = [y for y in np.random.randint(300, 10000, size=7)]
    plt.plot(years, gdp, color='g')
    plt.show()

if __name__ == '__main__':
    # plot()
    # plot1()
    # plot2()
    pass