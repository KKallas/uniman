"""Open the configured robot in the MuJoCo viewer (sim only, safe to run).

    uv run python -m uniman.view            # Linux
    uv run mjpython -m uniman.view          # macOS
    uv run python -m uniman.view --headless # load + step only, no window
"""

import sys

import mujoco
import mujoco.viewer

from .config import Config


def main():
    cfg = Config()
    if not cfg.scene_xml.exists():
        sys.exit(f"{cfg.scene_xml} not found; run ./scripts/setup.sh first")

    model = mujoco.MjModel.from_xml_path(str(cfg.scene_xml))
    data = mujoco.MjData(model)
    print(f"loaded unitree_{cfg.model}: nq={model.nq} nu={model.nu} timestep={model.opt.timestep}")

    if "--headless" in sys.argv:
        for _ in range(500):
            mujoco.mj_step(model, data)
        print(f"stepped 500 steps, base height {data.qpos[2]:.3f} m")
        return

    mujoco.viewer.launch(model, data)


if __name__ == "__main__":
    main()
