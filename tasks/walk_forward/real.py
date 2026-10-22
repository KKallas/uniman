"""Walk 1 m forward, then turn 90°. Run by a human only, with the e-stop in hand:

    UNIMAN_IFACE=en7 uv run --extra real python tasks/walk_forward/real.py
"""

import math

from uniman.real import RealRobot


def main():
    input("Robot standing, area clear, remote in hand? Press Enter to start (Ctrl-C to abort)...")
    with RealRobot() as robot:
        robot.move(vx=0.25, seconds=4.0)  # ~1 m
        robot.move(vx=0.0, vyaw=0.4, seconds=(math.pi / 2) / 0.4)


if __name__ == "__main__":
    main()
