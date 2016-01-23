#!/usr/bin/python3

# eq1 --> (M+m)x2dot - ml sinΘ Θdot^2 + ml cosΘ Θ2dot = u
# eq1 --> m x2dot cosΘ + ml Θ2dot = mg sinΘ


from math import sin, cos, pi, degrees
from scipy import arange

g = 9.8 #gravity acceleration constant (m/s**2)


class InvertedPendulum (object):

    def __init__(self):
        self.M = 10  #kg mass of cart
        self.m = 1   #kg mass of pendulum
        self.l = 1   #lenght of pendulum arm

    def __getLinearAccelleration2(self, u=1, theta=0, thetadot=0):
        # Calculates the linear acceleration
        a = u + \
            (self.m * self.l * sin(theta) * thetadot**2) - \
            (self.m * g * cos(theta) * sin(theta))
        b = self.M + self.m - (self.m * cos(theta)**2)

        x2dot = a/b
        return x2dot


    def __getAngularAccelleration2(self, u=1, theta=0, thetadot=0):
        M = self.M + self.m
        a = (u * cos(theta)) - (M * g * sin(theta)) + (self.m * self.l * (cos(theta) * sin(theta)) * thetadot)
        b = (self.m * self.l * (cos(theta)**2)) - (M * self.l)

        Θ2dot = a / b
        return Θ2dot


    def __getInstantaneousVelocity(self, xdot, x2dot, seconds):
        try:
            return xdot + (x2dot * seconds)
        except ZeroDivisionError:
            return xdot


    def __getInstAngularVelocity(self, thetadot, theta2dot, seconds):
        try:
            return thetadot + (theta2dot * seconds)
        except ZeroDivisionError:
            return thetadot

    def applyforce(self, u=1, tmax=10, timeslice=0.01):
        try:
            xArray = []
            thetaArray = []

            x = 0
            xdot = 0
            theta = 0
            thetadot = 0

            x2dot = self.__getLinearAccelleration2(u, theta, thetadot)
            theta2dot = self.__getAngularAccelleration(x2dot, theta)

            xdot = self.__getInstantaneousVelocity(xdot, x2dot, tmax)
            thetadot = self.__getInstAngularVelocity(thetadot, theta2dot, tmax)

            for t in arange(timeslice, tmax, timeslice):
                x = x + (xdot * timeslice)
                theta = theta + (thetadot * timeslice)

                print('Position -> {0}'.format(x))
                print('Theta -> {0} - {1}'.format(theta, degrees(theta)))

                xArray.append(x)
                thetaArray.append(theta)

            return xArray, thetaArray
        except Exception as ex:
            print(ex)


    #region Deprecated Functions

    def __getLinearAccelleration(self, u=1, theta=0, thetadot=0, theta2dot=0):
        # x2dot = ( ml sinΘ Θdot^2 - ml cosΘ Θ2dot + u) / (M+m)
        # Calculates the linear acceleration
        x2dot = ((self.m * self.l * sin(theta) * (thetadot**2)) -
                 (self.m * self.l * cos(theta) * theta2dot) + u) / \
                (self.M + self.m)
        return x2dot

    def __getAngularAccelleration(self, x2dot=0, theta=0):
        Θ2dot = ((g * sin(theta)) - (x2dot * cos(theta))) / self.l
        return Θ2dot

    def __getLinearVelocity(self, xdot, x2dot, t):
        try:
            return xdot + (x2dot * t)
        except ZeroDivisionError:
            return xdot

    def __getAngularVelocity(self, thetadot, theta2dot, t):
        try:
            return thetadot + (theta2dot * t)
        except ZeroDivisionError:
            return thetadot

    #endregion
