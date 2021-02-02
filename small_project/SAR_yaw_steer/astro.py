import numpy as np

GM_earth = 3.986004418e14
earth_rotation_rate = 7.2921150e-5

def orbit_period(semimajor_axis):
    return np.sqrt( 4*np.pi**2 * semimajor_axis**3 / GM_earth ) # Kepler's Third laws of planetary motion

def orbit_angular_rate(semimajor_axis):
    return 2*np.pi / orbit_period(semimajor_axis)