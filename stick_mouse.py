"""
Script to control mouse cursor with gamepad stick.
Specifically: right stick x axis controls mouse x position.
Requires FreePIE: https://github.com/AndersMalmgren/FreePIE
2020-06-11 JAO
"""

if starting:
    """This block only runs once."""
    import time
    joy_id = 0 # gamepad device number
    x_axis_mult = 0.25 # pos mode movement multiplier

def axis_to_mouse_pos(axis):
    """Position Mode. Stick deflection sets relative mouse cursor position."""
    return filters.delta(axis) * x_axis_mult

frame_start = time.time() # setup frame limiter
mouse.deltaX = axis_to_mouse_pos(axis=joystick[joy_id].xRotation)
time.sleep(max(1./60 - (time.time() - frame_start), 0)) # frame limiter
