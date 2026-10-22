"""High-level real-robot client. Only humans run scripts that import this (see CLAUDE.md).

Wraps the Unitree SDK's locomotion service (G1/H1: LocoClient, Go2: SportClient)
and routes every motion command through uniman.safety.
"""

import time

from .config import Config
from .safety import MAX_MOVE_SECONDS, clamp_velocity


class RealRobot:
    def __init__(self, cfg: Config | None = None):
        from unitree_sdk2py.core.channel import ChannelFactoryInitialize

        self.cfg = cfg or Config()
        ChannelFactoryInitialize(0, self.cfg.network_interface)

        if self.cfg.model == "go2":
            from unitree_sdk2py.go2.sport.sport_client import SportClient

            self._client = SportClient()
        elif self.cfg.model == "h1":
            from unitree_sdk2py.h1.loco.h1_loco_client import LocoClient

            self._client = LocoClient()
        else:
            from unitree_sdk2py.g1.loco.g1_loco_client import LocoClient

            self._client = LocoClient()
        self._client.SetTimeout(10.0)
        self._client.Init()

    def move(self, vx: float, vy: float = 0.0, vyaw: float = 0.0, seconds: float = 1.0):
        vx, vy, vyaw = clamp_velocity(vx, vy, vyaw)
        seconds = min(seconds, MAX_MOVE_SECONDS)
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            self._client.Move(vx, vy, vyaw)
            time.sleep(0.05)
        self.stop()

    def stop(self):
        self._client.StopMove()

    def damp(self):
        """Go limp. Use this when anything looks wrong."""
        self._client.Damp()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.stop()
