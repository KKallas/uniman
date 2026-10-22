# Task: walk_forward

## Goal
A first hardware sanity check: walk 1 m forward, stop, turn 90°, stop.

## Reference
None.

## Scene
Flat floor only.

## Success criteria
On hardware, the robot ends within 0.2 m and 15° of the target without stumbling.

## Limits
vx ≤ 0.3 m/s, vyaw ≤ 0.5 rad/s (inside the defaults in `uniman/safety.py`).

## Approach
Use the built-in high-level locomotion service. There's no sim step because the service exists only on the robot, so the first run is on the gantry.

## Status
- [x] Spec agreed
- [x] real.py written
- [ ] Gantry run on hardware
- [ ] Free run on hardware
