"""Just writing this so you can fill in the functions, hopefully should add clarity about
the structure of the algorithm"""

import numpy as np

"""
No C like struct available in Python, so a class will do for now.
"""


class VehicleVelocity():
    """
    Vector of vehicle velocity
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.mag = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        



class InertialForces:
    """
    Vector of acceleration components felt by car
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.mag = np.sqrt(x ** 2 + y ** 2 + z ** 2)





def turning_radius_meters(v_mps, steering_angle_rad):
    """
    :param v_mps: Vehicle velocity. x and y components can be accesses with v_mps.x and
    v_mps.y respecitvely.
    :param steering_angle_rad: Steering angle in radians
    :return: The turn radius of a perfect circle if v_mps and steering_angle_rad are constants
    """
    print(v_mps, steering_angle_rad)
    return 0

def ideal_acceleration(v_mps, turn_r_m):
    """
    :param v_mps: Vehicle velocity. x and y components can be accesses with v_mps.x and
    v_mps.y respecitvely.
    :param turn_r_m: Instantaneous effective turn radius of perfect circle
    :return: Vector of ideal instantaneous acceleration the CG should feel corresponding to
    ideal slip angle
    """
    print(v_mps, turn_r_m)
    return 0

def acceleration_error(ideal_accel, actual_accel):
    return 0