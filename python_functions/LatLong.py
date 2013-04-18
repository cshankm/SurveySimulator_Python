def LatLong(pos):
    """Transform cartesian coordinates into longitude, latitude and distance.

    If the input coordiates are in the International Celestial Reference Frame
    (ICRF) the output is in RA and DEC.

    ---------------------------------------------------------------------------

    Written by J-M. Petit Observatoire de Besancon
    Version 1 : February 2004

    Ported to Python by Cory Shankman University of Victoria
    Version 1 : April 2013

    ---------------------------------------------------------------------------

    INPUT:
    pos   : Object's cartesian coordinates (x,y,z)

    RETURN:
    long  : Longitude (RA if ICRF)
    lat   : Latitude (DEC if ICRF)
    r     : Distance to centre

    long, lat, r = LatLong(pos)

    ---------------------------------------------------------------------------

    CALLS:
    none

    CALLED BY:
    RADECeclXV

    """

    r = math.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2)
    long = math.atan2(pos[1], pos[0])
    if long > 0:
        long += 2.0 * math.pi
    lat = math.asin(pos[2] / r)

    return long, lat, r
