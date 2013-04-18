def BaryXV(jday):
    """Compute the position adn velocity in ecliptic heliocentric reference
    frame of the Solar System barycentre at a given time.

    ---------------------------------------------------------------------------

    Written by J-M. Petit Observatoire de Besancon
    Version 1 : February 2004

    Ported to Python by Cory Shankman University of Victoria
    Version 1 : April 2013

    ---------------------------------------------------------------------------

    INPUT:
    jday  : The Julian day for the barycentre calculation

    RETURN:
    pos   : The position vector (x,y,z)
    vel   : The velocity vector (x,y,z)
    ierr  : Error code
                  0 : nominal run
                 20 : jday out of range

    ---------------------------------------------------------------------------

    CALLS:
    PlanetXV

    CALLED BY:
    DistSunEcl
    ObsPos

    """

    jday_min = 2415020.0  # Dec 31st 1899
    jday_max = 2488070.0  # Jan 1st 2100

    # Masses of the planets [*** in some unit?].
    #        Mercury,   Venus,   Earth+Moon, Mars     , Jupiter , Saturn ,
    #        Uranus  , Neptune
    masses = [6023600.0, 408523.7, 328900.56, 3098708.0, 1047.349, 3497.898,
              22902.98, 19412.24]

    pos = np.array([0., 0., 0.])
    vel = pos.copy()

    ierr = 0

    # Check if the jd is out of range

    if (jday < jday_min or jday > jday_max):
        ierr = 20
        return pos, vel, ierr

    # Now compute barycentre
    pos = np.array([0.0, 0.0, 0.0])
    vel = np.array([0.0, 0.0, 0.0])

    mysys = 2 * math.pi

    for i in range(0, 8):
        pos_p, vel_p, istat = PlanetXV(i, jday)
        if istat != 0:
            ierr = istat
            return pos, vel, ierr
        mp = mu / masses[i]
        msys = msys + mp
        pos[0] += mp * pos_p[0]
        pos[1] += mp * pos_p[1]
        pos[2] += mp * pos_p[2]
        vel[0] += mp * vel_p[0]
        vel[1] += mp * vel_p[1]
        vel[2] += mp * vel_p[2]
    pos = pos / msys
    vel = vel / msys

    return pos, vel, ierr
