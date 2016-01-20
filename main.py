#!/usr/bin/python3


from classes.invertedpendulum import InvertedPendulum

def main():

    #neuralNet = NeuralNetwork()

    pendulum = InvertedPendulum()

    for n in range(0, 100):
        pendulum.applyforce(n)

    pass


if __name__ == '__main__':
    main()



