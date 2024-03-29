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

def lineStyle():
    t = np.arange(0, 5, 0.2)
    a = plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()
    print(a)

def lineWidth():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y, linewidth = 3.0)
    plt.plot(x, y)
    plt.show()

def lineMarker():
    years = [x for x in range(1950, 2011, 10)]
    gdp = [y for y in np.random.randint(300, 10000, size=7)]
    plt.plot(years, gdp, marker='o', markersize=6, markeredgewidth=1,
             markeredgecolor='red', markerfacecolor='green')
    plt.show()

def lineMarker1():
    plt.plot([1, 2, 3, 4], 'ro')
    plt.show()

def lineLabel():
    a = b = np.arange(0, 3, .02)
    c = np.exp(a)
    d = c[::-1]

    plt.plot(a, c, 'k--', label = 'Model length')
    plt.plot(a, d, 'k:', label = 'Data length')
    plt.plot(a, c+d, 'k', label='Total message length')
    plt.show()

def lineLegend():
    a = b = np.arange(0, 3, .02)
    c = np.exp(a)
    d = c[::-1]

    plt.plot(a, c, 'k--', label = 'Model length')
    plt.plot(a, d, 'k:', label = 'Data length')
    plt.plot(a, c+d, 'k', label='Total message length')

    plt.legend()
    plt.show()

def lineAxis():
    a = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    b = plt.axis([0, 6, 0, 20])
    plt.show()
    print(a)
    print(type(b), b)

def lineLabelTicks():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    width = 0.01
    ind = np.arange(N)
    print(ind)
    plt.bar(ind, menMeans)
    plt.title('Scores by group and gender')
    plt.ylabel('Scores')
    plt.xlabel('The number of people')
    plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend(('Men'))
    plt.show()

def lineLim():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.title('Plot of y sv x')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.xlim(0.0, 7.0)
    plt.ylim(0.0, 30.0)
    plt.show()

def scatter():
    data = np.random.rand(10, 2)
    print(data)
    print(data.shape)

    plt.scatter(data[:,0], data[:,1])
    plt.show()

def scatter1():
    x = np.random.rand(10)
    y = np.random.rand(10)
    z = np.sqrt(x**2 + y**2)
    plt.subplot(321)
    plt.scatter(x, y, s=80, c = z, marker='>')
    plt.show()

def barchart():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    width = 0.01
    ind = np.arange(N)
    print(ind)
    plt.bar(ind, menMeans)
    plt.show()

def Barh():
    w_pop = np.array([5, 30, 45, 40], dtype=np.float32)
    m_pop = np.array([4, 28, 40, 35], dtype=np.float32)
    x = np.arange(4)
    a = plt.barh(x, w_pop, color= 'r')
    b = plt.barh(x, -m_pop)
    print(a)
    print(b)
    plt.show()

def Pie():
    data = [5, 10, 30, 20, 7, 8, 10, 10]
    plt.pie(data)
    plt.show()

def hist():
    data = np.random.normal(5.0, 3.0, 1000)
    plt.hist(data)
    plt.xlabel('data')
    plt.show()

def hist1():
    data = np.random.normal(5.0, 3.0, 1000)
    plt.hist(data, bins=15, facecolor='red', alpha=0.4)
    plt.xlabel('data')
    plt.show()

def file_read():
    X, Y = [], []
    for line in open('./Matplotlib/data.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])
    plt.plot(X, Y)
    plt.show()


if __name__ == '__main__':
    # plot()
    # plot1()
    # plot2()
    # lineStyle()
    # lineWidth()
    # lineMarker()
    # lineMarker1()
    # lineLabel()
    # lineLegend()
    # lineAxis()
    # lineLabelTicks()
    # lineLim()
    # scatter()
    # scatter1()
    # barchart()
    # Barh()
    # Pie()
    # hist()
    # hist1()
    file_read()
    pass