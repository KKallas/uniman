# CLAUDE.md

This repo teaches a Unitree walking robot (default: G1 humanoid) new tasks through a sim-first pipeline. See README.md for the overview.

## Hard rules

1. **Never run anything that commands the real robot.** That means anything using `uniman.real`, `ChannelFactoryInitialize(0, ...)`, or a non-loopback network interface. Write the script, then tell the user the exact command to run themselves. Real-robot runs are always started by a human with the e-stop in hand.
2. **Sim first.** No task goes near hardware until it meets the success criteria in its `TASK.md` in MuJoCo, across several seeds or randomized starts.
3. **Respect `uniman/safety.py`.** Every real-robot command goes through its clamps. Don't raise the limits unless the user explicitly asks, and mention it whenever you change them.
4. **Don't guess robot-specific facts** (joint order, DDS topic names, IPs, SDK method names). Check them in `third_party/` (cloned by `scripts/setup.sh`) or the upstream docs.

## Workflow per task

1. `tasks/<name>/TASK.md`: copy from `tasks/_template/`. Fill in the goal, scene, success metric and limits. If the user gives a video, put it in `videos/` and describe the motion phases you see in it.
2. `tasks/<name>/scene.xml`: a MuJoCo scene that `<include>`s the robot from `third_party/mujoco_menagerie/unitree_<model>/` and adds the props.
3. `tasks/<name>/controller.py`: start with the simplest thing that can work, such as a scripted high-level motion or keyframes. Move to RL (`third_party/unitree_rl_gym`) only when that isn't enough.
4. `tasks/<name>/eval.py`: run headless, compute the success metric, write `results/summary.json` and optionally an mp4.
5. `tasks/<name>/real.py`: the hardware version. It uses `uniman.real` and goes through the safety clamps. Hand it to the user; don't run it.

## Commands

- `uv sync`: install deps
- `./scripts/setup.sh`: clone upstream repos and models into `third_party/`
- `uv run python -m uniman.view`: open the robot in the viewer (`mjpython` on macOS)
- `uv run python tasks/<name>/eval.py`: headless sim eval (safe to run)

## Notes

- In `unitree_mujoco`, the sim uses DDS domain 1 on `lo`; the real robot uses domain 0 on the Ethernet interface.
- The high-level locomotion service (`LocoClient` / `SportClient`) exists only on the real robot. In sim, walking needs a locomotion policy (for example from `unitree_rl_gym`'s `deploy_mujoco`) or a scripted controller.
- Keep each task self-contained in its folder. Shared code goes in `uniman/`.
