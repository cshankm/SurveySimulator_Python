def PlanetXV(ind,jday):
    """Call PlanetElem to compute the position and velocity of a planet in 
    the eclliptic heliocentric reference frame for a given time.

    ---------------------------------------------------------------------------

    Written by J-M. Petit Observatoire de Besancon
    Version 1 : February 2004

    Ported to Python by Cory Shankman University of Victoria
    Version 1 : April 2013 
    
    ---------------------------------------------------------------------------

    INPUT:
    ind   : The planet index
              0 : Mercury
              1 : Venus
              2 : Earth + Moon
              3 : Mars
              4 : Jupiter
              5 : Saturn
              6 : Uranus
              7 : Neptune
    jday  : The Julian day for the barycentre calculation

    RETURN:
    pos   : The position vector (x,y,z)
    vel   : The velocity vector (x,y,z)
    ierr  : Error code
                  0 : nominal run
                 10 : Unknown planet index
                 20 : jday out of range

    ---------------------------------------------------------------------------

    CALLS:
    PlanetElem
    coord_cart

    CALLED BY:
    BaryXV

    """
    
    
    jday_min = 2415020.0 # Dec 31st 1899
    jday_max = 2488070.0 # Jan 1st 2100

    # Masses of the planets [*** in some unit?].
    #        Mercury,   Venus,   Earth+Moon, Mars     , Jupiter , Saturn  , 
    #        Uranus  , Neptune
    masses = [6023600.0, 408523.7, 328900.56, 3098708.0, 1047.349, 3497.898, 
             22902.98, 19412.24]
    
    pos = np.array([0., 0., 0.])
    vel = pos.copy()

    # Check planet index
    if ( ind < 0 or ind > 7):
        ierr = 20
        return pos, vel, ierr

    
    # Check if the jd is out of range
    if ( jday < jday_min or jday > jday_max):
        ierr = 20
        return pos, vel, ierr

    # Compute the planet's position
    a, e, inc, node, peri, capm, istat = PlanetElem(ind,jday)
    if istat != 0:
        ierr = istat
        return pos, vel, ierr

    gm = 2*math.pi*(1.0+1.0/masses[ind])
    pos, vel = coord_cart(gm, a, e, inc, node, peri, capm)

    return pos, vel, ierr
