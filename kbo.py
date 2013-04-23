#!/usr/bin/python
from random import random
import math
import ephem

class kbo(ephem.EllipticalBody):
    'Class for all KBOs in a survey simulator'

    __simdetections = 0

    def __init__(self, a, e, inc, capom, argperi, H=5):
#        ephem.EllipticalBody.__init__()
        self.a = a
        self.e = e
        self.inc = inc
        self.Om = capom # degrees or radians?
        self.om = argperi
        self.H = H
        self._G = -0.12 # Hard coded by JM. "c Hard coded slope for magnitude ! Bad boy !"

#----------- a

    @property
    def a(self):
        """I'm the a property."""
        return self._a

    @a.setter
    def a(self, value):
        if not 0.0 <= value <= 10E6:
            raise ValueError('Bad a value. Ensure 0.0 < a < 10E6')
        self._a = value

#----------- e

    @property
    def e(self):
        """I'm the e property."""
        return self._e

    @e.setter
    def e(self, value):
        if not 0.0 <= value <= 1.0:
            raise ValueError('Bad e value. e must be between 0 and 1')
        self._e = float(value)

#----------- inc

    @property
    def inc(self):
        """I'm the inc property."""
        return self._inc

    @inc.setter
    def inc(self, value):
        if not 0.0 <= value <= 90:
            raise ValueError('Bad inclination value. Ensure 0.0 < inclination < 90 degrees')
        self._inc = value

#----------- Om

   @property
    def Om(self):
        """I'm the Om property."""
        return self._Om

    @Om.setter
    def Om(self, value):
        if not 0.0 <= value <= 360.0:
            raise ValueError('Bad Om value. Om must be between 0 and 360 degrees')
        self._Om = float(value)

#----------- om

   @property
    def om(self):
        """I'm the om property."""
        return self._om

    @om.setter
    def om(self, value):
        if not 0.0 <= value <= 360.0:
            raise ValueError('Bad om value. om must be between 0 and 360 degrees')
        self._om = float(value)

#----------- H

   @property
    def H(self):
        """I'm the H property."""
        return self._H

    @H.setter
    def H(self, value):
        self._H = float(value)

#----------- epoch

   @property
    def epoch(self):
        """I'm the epoch property."""
        return self._epoch

    @epoch.setter
    def epoch(self, value):
        self._epoch = float(value)

#----------- epoch_M

   @property
    def epoch_M(self):
        """I'm the epoch_M property."""
        return self._epoch_M

    @epoc_M.setter
    def epoch_M(self, value):
        self._epoch_M = float(value)

#----------- M

   @property
    def M(self):
        """I'm the M property."""
        return self._M

    @M.setter
    def M(self, value):
        if not 0.0 <= value <= 360.0:
            raise ValueError('Bad M value. M must be between 0 and 360 degrees')
        self._M = float(value)



#------------------------------- Object Status --------------------------------

    def params(self):
        """Print the current orbital parameters a, e, inc, argperi, capom, H"""
        print "a is ", self.a
        print "e is ", self.e
        print "inclination is ", self.inc
        print "argument of pericentre is ", self.argperi
        print "Capital Omega is ", self.capom
        print "The H-mag is ", self.H
