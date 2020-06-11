"""
Script to control mouse cursor with gamepad stick.
Specifically: right stick x axis controls mouse x speed.
Requires FreePIE: https://github.com/AndersMalmgren/FreePIE
2020-06-11 JAO
"""

if starting:
    """This block only runs once."""
    import time
    joy_id = 0 # gamepad device number
    x_axis_sens = 50 #  spd mode sensitivity
    x_axis_dead = 3 # spd mode dead zone to prevent drifting

def axis_to_mouse_spd(axis):
    """Speed Mode. Stick deflection sets mouse cursor movement speed."""
    output = filters.mapRange(axis, -1000, 1000, -x_axis_sens, x_axis_sens)
    output = filters.deadband(output, x_axis_dead)
    return output

frame_start = time.time() # setup frame limiter
mouse.deltaX = axis_to_mouse_spd(axis=joystick[joy_id].xRotation)
time.sleep(max(1./60 - (time.time() - frame_start), 0)) # frame limiter
