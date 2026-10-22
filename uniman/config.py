import os
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
THIRD_PARTY = REPO_ROOT / "third_party"

MODELS = {"g1", "h1", "go2"}


@dataclass
class Config:
    model: str = field(default_factory=lambda: os.environ.get("UNIMAN_MODEL", "g1"))
    # Ethernet interface connected to the robot (192.168.123.0/24)
    network_interface: str = field(default_factory=lambda: os.environ.get("UNIMAN_IFACE", "eth0"))

    def __post_init__(self):
        if self.model not in MODELS:
            raise ValueError(f"unknown model {self.model!r}, expected one of {sorted(MODELS)}")

    @property
    def menagerie_dir(self) -> Path:
        return THIRD_PARTY / "mujoco_menagerie" / f"unitree_{self.model}"

    @property
    def scene_xml(self) -> Path:
        return self.menagerie_dir / "scene.xml"
