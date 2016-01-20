#!/usr/bin/python3

# eq1 --> (M+m)x2dot - ml sinΘ Θdot^2 + ml cosΘ Θ2dot = u
# eq1 --> m x2dot cosΘ + ml Θ2dot = mg sinΘ


from math import sin, cos, pi
from scipy import arange

g = 9.8 #gravity acceleration constant (m/s**2)


class InvertedPendulum (object):

    def __init__(self):
        self.M = 10  #kg mass of cart
        self.m = 1   #kg mass of pendulum
        self.l = 1   #lenght of pendulum arm

        self.x = 0          #cart position at time t
        self.x2dot = 0      #x_dotdot second derivative with respect to time
        self.xdot = 0       #x_dot derivative with respect to time

        self.theta = 0      #pendulum arm angle at time t in rad
        self.thetadot = 0   #angularvelocity = 0
        self.theta2dot = 0  #angularacceleration = 0

        self.timeslice = 0.01   #sampling interval in seconds


    def __getLinearAccelleration(self, u=1):
        # x2dot = ( ml sinΘ Θdot^2 - ml cosΘ Θ2dot + u) / (M+m)
        # Calculates the linear acceleration
        x2dot = ((self.m * self.l * sin(self.theta) * self.thetadot**2) -
                 (self.m * self.l * cos(self.theta) * self.theta2dot) + u) / \
                (self.M + self.m)
        return x2dot


    def __getAngularAccelleration(self, x2dot):
        Θ2dot = ((g * sin(self.theta)) - (x2dot * cos(self.theta))) / self.l
        return Θ2dot

    #TODO Factor in time
    def __getLinearVelocity(self, x2dot):
        return self.xdot + x2dot

    def __getAngularVelocity(self, theta2dot):
        return self.thetadot + theta2dot



    #applies a u force in newtons to the pendulum
    def applyforce(self, u=1, tmax=100, timeslice=0.1):
        try:
            #Calculates the linear acceleration, and velocity
            x2dot = self.__getLinearAccelleration(u)

            #Calculates the angular acceleration
            theta2dot = self.__getAngularAccelleration(x2dot)

            print('Acceleration -> {0}'.format(x2dot))
            print('Angular acceleration -> {0}'.format(theta2dot))

            # Once we have acceleration we can calculate velocity and positions at time t
            x = 0
            theta = 0

            for n in arange(0, tmax, timeslice):
                xdot = self.__getLinearVelocity(x2dot)
                thetadot = self.__getAngularVelocity(theta2dot)

                x = x + (xdot * timeslice)
                theta = theta + (thetadot * timeslice)

                print('Position -> {0}'.format(x))
                print('Theta -> {0}'.format(theta))

        except Exception as ex:
            print(ex)


   #def applyforce(self, u=0.01, x=0, xdot=0, x2dot=0, theta=0, theta2dot=0):
#    pass

