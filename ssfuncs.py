#!/usr/bin/python
from random import random
import math

#-------------------------- Size Distribution ---------------------------------


def drawH(alpha, hmax, alpha_faint=None, contrast=1, hbreak=None, 
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
        return  math.log10(rv*(hfaint - hbright) + hbright) / alpha
    else:
        rv = random()
        hbright = 10**(alpha_faint*hbreak)
        hfaint = 10**(alpha_faint*hmax)
        return  math.log10(rv*(hfaint - hbright) + hbright) / alpha_faint



#----------------- Fuzzing Variables a,e,inc, argperi, capom ------------------

def fuzz(var, fz, type=None):
    """Perturb (fuzz) semimajor axis randomly by up to +- percent specified
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
    fz = fz/100.0 if (fz > 1.0 and type is None) else fz
    var = (var*(1.0 + fz*(2.0*random()-1.0)) if type is None else
           (var + (2.0*random()-1.0)*fz))
    return var

#    def efuzz(self, efz, type=None):
#        efz = efz/100.0 if efz>1.0 else efz
#        self.e = (self.e*(1.0 + efz*(2.0*random()-1.0)) if type is None else
#                 (self.e + (2.0*random()-1.0)*efz))

#    def ifuzz(self, ifz, type=None):
#        ifz = ifz/100.0 if (ifz>1.0 and type is None) else ifz
#        self.inc = (self.inc*(1. + ifz*(2.*random()-1.)) if type is None else
#                 (self.inc + (2.0*random()-1.0)*ifz))

