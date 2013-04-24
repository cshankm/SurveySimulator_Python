#!/usr/bin/python
from random import random
import math
import ephem
# import field
# to be implemented once the field class has been created


class ssobj(ephem.EllipticalBody):
    'Class for all Survey Simulator objects.'

    def __init__(self, a, e, inc, capom, argperi, H=5, M=0.0):
#        ephem.EllipticalBody.__init__()
        self.a = a
        self.e = e
        self.inc = inc # degrees
        self.Om = capom # degrees 
        self.om = argperi # degrees
        self.H = H
        self.M = M
        self._G = -0.12 # Hard coded by JM: "c Hard coded slope for magnitude ! Bad boy !"


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
        if not 0.0 <= value <= 180.0:
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

    @epoch_M.setter
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

    def __str__(self):
        """Print the current orbital parameters a, e, inc, argperi, capom, H"""
        status = ("\na: %.2f \n" % self.a +
                  "e: %.2f \n" % self.e +
                  "inc: %.2f deg \n" % (self.inc * 180/math.pi) +
                  "om: %.2f deg \n" % (self.om * 180/math.pi) +
                  "Om: %.2f deg \n" % (self.Om * 180/math.pi) +
                  "H: %.2f \n" % self.H
                  )
        return status

#-------------------------- Size Distribution ---------------------------------


    def drawH(self, alpha, hmax, alpha_faint=None, contrast=1, hbreak=None,
              hmin=1):
        """Compute and assign and H-magnitude from a so-called singlE
        power-law, knee, or divot H-magnitude distribution.

        When provided a slope alpha and a faint-side maximum H-magnitude
        (hmax), a H-magnitude is drawn randomly from the distribution
                           dN/dH propto 10**(alpha H)
        in the range hmin = 1 to hmax. Specify hmin to change the bright-end.

        Specifying an hbreak and alpha_faint will draw from a knee distribution

        Specifying an hbreak, alpha_faint and contrast will draw from a divot
        distrubtion as in Shankman et al. 2013

        e.g.

        ---Single Power Law---

        object.drawH(0.8,13)

        will draw an H-magnitude from the appropriate distribution such that
        H [1,13]

        object.drawH(0.8,13,hmin=5)

        will draw an H-magnitude such that H [5,13]

        ---Knee---

        To draw from a knee distribution specify hbreak and alpha_faint

        object.drawH(0.8, 13, hbreak=9, alpha_faint = 0.5)

        This will draw an H-magnitude from a distrubtion that breaks at H=9
        from a slope of 0.8 to a slope of 0.5. hmin can also be specified here.


        ---Divot---

        To draw from a divot (see Shankman et al 2013), specify hbreak,
        alpha_faint, and the contrast value. Contrasts should be > 1.
        hmin can also be specified.

        object.drawH(0.8, 13, hbreak=9, alpha_faint = 0.5, contrast = 23)


        """

        # Avoid singularity for alpha = 0
        alpha = 0.0000000001 if alpha == 0 else alpha
        # Set alpha_faint to alpha for the case of a single power-law
        alpha_faint = alpha if alpha_faint is None else alpha_faint
        # Avoid singularity for alpha_faint = 0
        alpha_faint = 0.0000000001 if alpha_faint == 0 else alpha_faint
        # Set hbreak to be the maximum H for the case of a single power-law
        hbreak = hmax if hbreak is None else hbreak

        # ckc is the fraction of objects big (H<Hbreak) of the break
        # (with contrast cont >= 1 as in Shankman et al. 2013)
        ckc = (1.0 + 1.0 / contrast * alpha / alpha_faint *
               (10**(alpha_faint*(hmax - hbreak)) - 1.0))**(-1.0)

        rv = random()
        if (rv < ckc):
            rv = random()
            hbright = 10**(alpha*hmin)
            hfaint = 10**(alpha*hbreak)
            self.H = math.log10(rv*(hfaint - hbright) + hbright) / alpha

        else:
            rv = random()
            hbright = 10**(alpha_faint*hbreak)
            hfaint = 10**(alpha_faint*hmax)
            self.H = math.log10(rv*(hfaint - hbright) + hbright) / alpha_faint


#----------------- Fuzzing Variables a,e,inc, argperi, capom ------------------

    def fuzz(self, variable, fz, type=None):
        """Perturb (fuzz) semimajor axis randomly by up to +- percent specified
        Input is treated as percentage if type is not specified as 'abs'.
        If type = 'abs', a will be changed randomly by +- amount specified.

        The first argument is a string containing the variable to be fuzzed.
        The appropriate options are 'a', 'e', 'inc', 'Om', 'om' 

        e.g.
                   # KBO(a, e, inc, argperi, capom)
        object = ssobj(75, 0.5, 12, 45, 60)
        object.fuzz('a', 0.1)

        this will take a and randomly perturb it by +- 10%

        object.fuzz('a', 10)

        produces the same result

        ---

        Conversely,

        object.fuzz('a', 0.1, type='abs')

        pertubs a by +- 0.1 AU, and

        object.fuzz('a', 10, type='abs')

        perturbs a by +- 10 AU

        """
        # Check to see if the attribute exists, if so get the value
        if not hasattr(self, variable):
            raise ValueError("You tried to fuzz a parameter that does not exit")
        var = getattr(self, variable)
        # if variable is an angle, treat it properly as 
        # float(ephem.EllipticalBody().inc) gives the angle in radians
        if variable in ['inc', 'om', 'Om']:
            var = float(var)*180.0/math.pi
        # set fuzzer to percent
        fz = fz/100.0 if (fz > 1.0 and type is None) else fz
        var = (var*(1.0 + fz*(2.0*random()-1.0)) if type is None else
               (var + (2.0*random()-1.0)*fz))
        setattr(self, variable, var)


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- Detect *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class detect(object):

    fuzzedvars =[]

    @classmethod
    def load_survey(cls, path):
        # Empty dictionary to contain all of the field objects in the class
        cls.fields = {}
        # path to pointing.list directory
        # create field objects for every pointing which are shared by the class

    @classmethod
    def hdraw(cls, *args):
        pass

    @classmethod
    def fuzz_objects(cls, *args):
#        cls.fuzzed = True  # Probably unnecessary

        options = ['a', 'e', 'inc', 'Om', 'om']
        for item in args:
            if not item[0] in options:
                raise ValueError('Your given input of ' + item[0] + ' is not of a fuzzable variable')
            if not item[2] is 'abs':
                rais ValueError("The third argument for fuzz_objects MUST be 'abs' if specified")
            if len(item) > 3:
                raise ValuError("Specify the variable to be fuzzed and the amount e.g. ('inc', 1, 'abs')")

        cls.fuzzedvars = args

    @classmethod
    def load_file(cls, filepath, *args):
        cls.filepath = filepath
        # 
        # take in the order of the variables in the file as a tuple
        # i.e. ss.loadfile(path, ('inc',1), ('a',2)) counting from 0
        options = ['a', 'e', 'inc', 'Om', 'om', 'H', 'M', 'M_epoch']

        for item in args:
            if not item[0] in options:
                raise ValueError('Your given input of ' + item[0] + ' is not of the appropriate read-in type')
            if len(item) > 2:
                raise ValuError("Specify the variable and column of the variable in the form ('a', 0), counting from 0")
        cls.elementorder = args

    @classmethod
    def numdetections(class, numdetections):
        cls.numdetections = numdetections

    @classmethod
    def output(cls, outputfile):
        cls.outputfile = outputfile

    def __init__(self, external_candidate):
        # Take in the cadidate object and 
        # do all of the actual detection stuff. 
        pass
# Probably also write out for successful detections

