#!/usr/bin/python
from random import random
import math


class kbo(object):
    'Class for all KBOs in a survey simulator'

    __simdetections = 0

    def __init__(self, a, e, inc, capom, argperi, H=5):
        self.a = a
        self.e = e
        self.inc = inc
        self.capom = capom # degrees or radians?
        self.argperi = argperi
        self.H = H

    @property
    def a(self):
        """I'm the a property."""
        return self._a

    @a.setter
    def a(self, value):
        if not 0.0 <= value <= 10E6:
            raise ValueError('Bad a value. Ensure 0.0 < a < 10E6')
        self._a = value

    @property
    def e(self):
        """I'm the e property."""
        return self._e

    @e.setter
    def e(self, value):
        if not 0.0 <= value <= 1.0:
            raise ValueError('Bad e value. e must be between 0 and 1')
        self._e = float(value)

    @property
    def inc(self):
        """I'm the a property."""
        return self._inc

    @inc.setter
    def inc(self, value):
        if not 0.0 <= value <= 90:
            raise ValueError('Bad inclination value. Ensure 0.0 < inclination < 90 degrees')
        self._inc = value


#------------------------------- Object Status --------------------------------

    def params(self):
        """Print the current orbital parameters a, e, inc, argperi, capom, H"""
        print "a is ", self.a
        print "e is ", self.e
        print "inclination is ", self.inc
        print "argument of pericentre is ", self.argperi
        print "Capital Omega is ", self.capom
        print "The H-mag is ", self.H
