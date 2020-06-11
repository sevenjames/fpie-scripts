"""
Script to control mouse cursor with gamepad stick.
Requires FreePIE: https://github.com/AndersMalmgren/FreePIE
Currently configured for right stick x axis control of mouse x position.
2020-06-11 JAO

FreePIE scripts automatically loop too fast.
This is managed with a "starting" block and a frame limiter.

Inputs reference for Logitech F310 gamepad:
left stick LR = x axis, left stick UD = y axis
right stick LR = x rotation, right stick UD = y rotation
left trigger = +z axis, right trigger = -z axis
"""

if starting:
    """This block only runs once."""
    import time
    joy_id = 0 # gamepad device number
    x_axis_mult = 0.25 # pos mode movement multiplier
    x_axis_sens = 50 #  spd mode sensitivity
    x_axis_dead = 3 # spd mode dead zone to prevent drifting

def axis_to_mouse_pos(axis):
    """Position Mode. Stick deflection sets relative mouse cursor position."""
    return filters.delta(axis) * x_axis_mult

def axis_to_mouse_spd(axis):
    """Speed Mode. Stick deflection sets mouse cursor movement speed."""
    output = filters.mapRange(axis, -1000, 1000, -x_axis_sens, x_axis_sens)
    output = filters.deadband(output, x_axis_dead)
    return output

frame_start = time.time() # setup frame limiter
#Only call one of the two binding functions here:
mouse.deltaX = axis_to_mouse_pos(axis=joystick[joy_id].xRotation)
time.sleep(max(1./60 - (time.time() - frame_start), 0)) # frame limiter
