# FreePIE script for mouse cursor control with gamepad stick.
# Specifically: right stick x axis for semi-absolute mouse cursor control.
# Can be modified for any analog axis for absolute or relative movement.
# 2020-03-02 JAO

# (!) FreePIE scripts are automatically looped as fast as possible; too fast.
# This is managed with a "starting" block and a frame limit timer.
# See documentation here: https://github.com/AndersMalmgren/FreePIE

# inputs reference for gamepad : Logitech F310
# left stick LR = X axis, left stick UD = Y axis
# right stick LR = X rotation, right stick UD = Y rotation
# left trigger = +Z axis, right trigger = -Z axis

if starting:
	# this section only runs once
	import time
	j_id = 0 # gamepad device number
	jrx_mult = 0.45 # movement range for absolute mode
	jrx_sens = 50 # sensitivity for relative mode
	jrx_dead = 3 # dead zone for relative mode to prevent drifting

def main_abs_mode():
	# semi-absolute mode: stick deflection sets mouse cursor position
	# is only semi because "origin" is based on cursor position, not screen
	# mouse cursor will return to "origin" when stick springs back to center
	jrx_in = joystick[j_id].xRotation
	jrx_delta = filters.delta(jrx_in)
	jrx_out = jrx_delta * jrx_mult
	mouse.deltaX = jrx_out

def main_rel_mode():
	# relative mode: stick deflection sets mouse cursor speed
	# mouse cursor speed will return to zero when stick springs back to center
	jrx_in = joystick[j_id].xRotation
	jrx_map = filters.mapRange(jrx_in, -1000, 1000, -jrx_sens, jrx_sens)
	jrx_out = filters.deadband(jrx_map, jrx_dead)
	mouse.deltaX = jrx_out

frame_start = time.time()
main_abs_mode() # only run one mode at a time
time.sleep(max(1./60 - (time.time() - frame_start), 0))
