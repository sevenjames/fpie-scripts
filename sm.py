"""minimized stick mouse"""

if starting:
    import time

frame_start = time.time()
mouse.deltaX = filters.delta(joystick[0].xRotation) * 0.25
time.sleep(max(1./60 - (time.time() - frame_start), 0))
