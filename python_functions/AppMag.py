def AppMag(r, delta, robs, h, g):
    """Compute phase angle and apparent magnitude.

    ---------------------------------------------------------------------------

    Written by J-M. Petit Observatoire de Besancon
    Version 1 : February 2004

    Ported to Python by Cory Shankman University of Victoria
    Version 1 : April 2013

    ---------------------------------------------------------------------------

    INPUT:
    r     : Sun-object distance (AU)
    delta : Earth-object distance (AU)
    robs  : Sun-Earth distance (AU)
    h     : Absolute magnitude of the object
    g     : Slope of the object (***huh?)

    RETURN:
    alpha : Phase angle
    mag   : Apparent magnitude
    ierr  : Error code
            0 : nominal run
            10: wrong input data

    alpha, mag, ierr = AppMag(r,delta,robs,h,g)


    ---------------------------------------------------------------------------

    CALLS:
    none

    CALLED BY:
    Detect
    Detect1

    """

    ierr = 0
    denom = 2.0 * r * delta
    if (denom == 0.0):
        ierr = 10
        alpha = 0
        mag = 0
        return

    alpha = math.acos((-robs**2.0 + delta**2.0 + r**2.0)/denom)
    phi1 = math.exp(-3.33*(math.tan(alpha/2.0))**0.63)
    phi2 = math.exp(-1.87*(math.tan(alpha/2.0))**1.22)
    mag = 5*math.log10(r*delta) + h - 2.5*math.log10((1.0 - g)*phi1 + g*phi2)

    return alpha, mag, ierr
