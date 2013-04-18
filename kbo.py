#!/usr/bin/python
from random import random
import math

class kbo:
    'Class for all KBOs in a survey simulator'

    __simdetections = 0

    def __init__(self, a, e, inc, capom, argperi):
        self.a = a
        self.e = e
        self.inc = inc
        self.capom = capom
        self.argperi = argperi
        self.H = 5 #assign arbitrary h value

#-------------------------- Size Distribution ---------------------------------

    def drawH(self, alpha, hmax, alpha_faint=None, contrast=1, hbreak = None, 
              hmin = 1):
        """Compute and assign and H-magnitude from a so-called single power-law,
        knee, or divot H-magnitude distribution.

        When provided a slope alpha and a faint-side maximum H-magnitude (hmax),
        a H-magnitude is drawn randomly from the distribution
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
        alpha_faint = alpha if alpha_faint is None else alpha_faint


        hbreak = hmax if hbreak is None else hbreak

        #ckc is the fraction of objects big of the knee/cliff (with contrast cont >= 1)
        ckc = (1.0 + 1.0/contrast*alpha/alpha_faint*(10**(alpha_faint*(hmax
               - hbreak))-1.0))**(-1.0) 

        rv = random() 
        if (rv < ckc):
            rv = random()
            hbright = 10**(alpha*hmin)
            hfaint = 10**(alpha*hbreak)
            self.H = math.log10( rv*(hfaint - hbright) +  hbright )/ alpha
        else:
            rv = random()
            hbright = 10**(alpha_faint*hbreak)
            hfaint = 10**(alpha_faint*hmax)
            self.H = math.log10( rv*(hfaint - hbright) +  hbright )/ alpha_faint
        print self.H


#----------------- Fuzzing Variables a,e,inc, argperi, capom ------------------

    def afuzz(self,afz,type=None):
        """Perturb (fuzz) semimajor axis randomly by up to +- percent specified.
        Input is treated as percentage if type is not specified as 'abs'.
        If type = 'abs', a will be changed randomly by +- amount specified.

        e.g.
               # KBO(a, e, inc, argperi, capom)  
        object = KBO(75, 0.5, 12, 45, 60)
        object.afuzz(0.1)
        
        this will take a and randomly perturb it by +- 10%

        object.afuzz(10) 
        
        produces the same result

        ---
        
        Conversely,

        object.afuzz(0.1, type='abs')

        pertubs a by +- 0.1 AU, and

        object.afuzz(10, type='abs')
        
        perturbs a by +- 10 AU

        """
        afz = afz/100.0 if (afz>1.0 and type is None) else afz
        self.a = (self.a*(1.0 + afz*(2.0*random()-1.0)) if type is None else 
                 (self.a + (2.0*random()-1.0)*afz))


    def efuzz(self,efz,type=None):
        efz = efz/100.0 if efz>1.0 else efz
        self.e = (self.e*(1.0 + efz*(2.0*random()-1.0)) if type is None else
                 (self.e + (2.0*random()-1.0)*efz))


    def ifuzz(self,ifz,type=None):
        ifz = ifz/100.0 if (ifz>1.0 and type is None) else ifz
        self.inc = (self.inc*(1. + ifz*(2.*random()-1.)) if type is None else
                 (self.inc + (2.0*random()-1.0)*ifz))
    

    def argfuzz(self,argfz,type=None):
        argfz = argfz/100.0 if (argfz>1.0 and type is None) else argfz
        self.argperi = (self.argperi*(1.0 + argfz*(2.0*random()-1.0)) if type 
                        is None else (self.argperi + (2.0*random()-1.0)*argfz))
    

    def omfuzz(self,omfz,type=None):
        omfz = omfz/100.0 if (omfz>1.0 and type is None) else omfz
        self.capom = (self.capom*(1.0 + omfz*(2.0*random()-1.0)) if type 
                      is None else (self.capom + (2.0*random()-1.0)*omfz))

    def fuzz(self,afz,efz,ifz,argfz,omfz,type=None):
       self.afuzz(afz,type)
       self.efuzz(efz,type)
       self.ifuzz(ifz,type)
       self.argfuzz(argfz,type)
       self.omfuzz(omfz,type)


#------------------------------- Object Status --------------------------------

    def params(self):
        """Print the current orbital parameters a, e, inc, argperi, capom."""
        print "a is ", self.a
        print "e is ", self.e
        print "inclination is ", self.inc
        print "argument of pericentre is ", self.argperi
        print "Capital Omega is ", self.capom
