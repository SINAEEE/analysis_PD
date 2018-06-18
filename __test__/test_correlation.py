
import matplotlib.pyplot as plt
import numpy as np

def ex1():
    height = [100,120,130,140,150,160,170,180,190]
    footsizes = [200,205,210,220,230,240,250,270,280]

    fig, subplots = plt.subplots(1,1)
    subplots.scatter(height,footsizes)

    plt.xlabel('키(cm)')
    plt.ylabel('발크기(mm)')

    plt.show()

def ex2():
    height = [100, 200, 330, 440, 550, 660, 770, 880, 990]
    temps = [18.5, 17.5, 17, 16, 15, 14, 13, 12.5, 1]

    fig, subplots = plt.subplots(1,1)
    subplots.scatter(height,temps)

    plt.xlabel('산의 높이(cm)')
    plt.ylabel('온도(℃)')

    plt.show()

def ex3():

    fig, subplots = plt.subplots(1,1)
    subplots.scatter(
        np.random.random_integers(0, 100, 50),
        np.random.random_integers(0, 100, 50)
    )

    plt.show()

if __name__ =='__main__':
    #ex1()
    #ex2()
    ex3()




