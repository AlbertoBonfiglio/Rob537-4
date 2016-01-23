#!/usr/bin/python3


from classes.invertedpendulum import InvertedPendulum
from fractions import Fraction
from math import sin, cos
import matplotlib.pyplot as plt
import numpy as np


def main():

    #neuralNet = NeuralNetwork()

    pendulum = InvertedPendulum()
    x = []
    O = []
    for n in np.arange(0.5, 10,1.5):
        x, O = pendulum.applyforce(u=n, tmax=5, timeslice=0.01)

        showGraph(O)



def showGraph(theta):
    r = 1
    x = []
    y = []
    for n in range(len(theta)):
        x.append(r*cos(theta[n]))
        y.append(r*sin(theta[n]))

    fig = plt.figure()
    ax  = fig.add_subplot(111)

    ax.plot(x,y,'b.')
    plt.show()


def x1():

    x=np.arange(-10.0,10.0,0.1)
    y=np.arctan(x)

    fig = plt.figure()
    ax  = fig.add_subplot(111)

    ax.plot(x,y,'b.')

    y_pi   = y/np.pi
    unit   = 0.25
    y_tick = np.arange(-0.5, 0.5+unit, unit)

    y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
    ax.set_yticks(y_tick*np.pi)
    ax.set_yticklabels(y_label, fontsize=20)

    y_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in y_tick]
    ax2 = ax.twinx()
    ax2.set_yticks(y_tick*np.pi)
    ax2.set_yticklabels(y_label2, fontsize=20)

    plt.show()


def create_pi_labels(a, b, step):

    max_denominator = int(1/step)
    # i added this line and the .limit_denominator to solve an
    # issue with floating point precision
    # because of floataing point precision Fraction(1/3) would be
    # Fraction(6004799503160661, 18014398509481984)

    values = np.arange(a, b+step/10, step)
    fracs = [Fraction(x).limit_denominator(max_denominator) for x in values]
    ticks = values*np.pi

    labels = []

    for frac in fracs:
        if frac.numerator==0:
            labels.append(r"$0$")
        elif frac.numerator<0:
            if frac.denominator==1 and abs(frac.numerator)==1:
                labels.append(r"$-\pi$")
            elif frac.denominator==1:
                labels.append(r"$-{}\pi$".format(abs(frac.numerator)))
            else:
                labels.append(r"$-\frac{{{}}}{{{}}} \pi$".format(abs(frac.numerator), frac.denominator))
        else:
            if frac.denominator==1 and frac.numerator==1:
                labels.append(r"$\pi$")
            elif frac.denominator==1:
                labels.append(r"${}\pi$".format(frac.numerator))
            else:
                labels.append(r"$\frac{{{}}}{{{}}} \pi$".format(frac.numerator, frac.denominator))

    return ticks, labels

if __name__ == '__main__':
    main()



