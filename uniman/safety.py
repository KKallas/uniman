"""Conservative limits applied to every real-robot command. Raise only deliberately."""

from dataclasses import dataclass


@dataclass(frozen=True)
class VelocityLimits:
    vx: float = 0.4  # m/s forward/back
    vy: float = 0.2  # m/s lateral
    vyaw: float = 0.5  # rad/s


LIMITS = VelocityLimits()

# Longest a single Move() may run before the caller has to re-issue it
MAX_MOVE_SECONDS = 5.0


def _clamp(v: float, lim: float) -> float:
    return max(-lim, min(lim, v))


def clamp_velocity(vx: float, vy: float, vyaw: float, limits: VelocityLimits = LIMITS):
    return _clamp(vx, limits.vx), _clamp(vy, limits.vy), _clamp(vyaw, limits.vyaw)
