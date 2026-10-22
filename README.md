# uniman

Use Claude Code to teach a Unitree walking robot new tasks: **describe or film a task → build it in simulation → validate → run it on the real robot.**

Inspired by DeepMind's [video-to-sim-to-real cornhole demo](https://youtu.be/9PICEmtfpWU), where a model watched a human play cornhole, rebuilt the scene in MuJoCo, worked out the whole-body control, and transferred the result to a real humanoid.

## Pipeline

```
 task idea / video ──► tasks/<name>/TASK.md ──► MuJoCo scene + controller ──► sim validation ──► real robot
                         (spec + success)         (tasks/<name>/)             (metrics, video)   (operator-gated)
```

1. **Spec.** Each task gets a folder in `tasks/` with a `TASK.md` that covers the goal, the scene, success criteria and safety limits.
2. **Sim.** Claude Code builds the MuJoCo scene (robot + props) and a controller or policy for it.
3. **Validate.** Run it in sim until it meets the success criteria consistently.
4. **Real.** A human operator runs it on hardware with the e-stop in hand. Real-robot runs are never automatic.

## Hardware

Defaults to the **Unitree G1** humanoid. You can switch to `h1` or `go2` in `uniman/config.py` or with `UNIMAN_MODEL`.

## Setup

```bash
# Python env + deps (MuJoCo, numpy, Unitree SDK)
uv sync

# Robot models from mujoco_menagerie + Unitree's sim/RL repos into ./third_party
./scripts/setup.sh

# Smoke test: open the robot in the MuJoCo viewer
uv run python -m uniman.view            # G1 by default
UNIMAN_MODEL=go2 uv run python -m uniman.view
```

On macOS, the interactive MuJoCo viewer must be started with `mjpython`: `uv run mjpython -m uniman.view`.

### Connecting to the real robot

1. Connect your PC to the robot over Ethernet.
2. Set a static IP on that interface: `192.168.123.99/24`.
3. Check the connection: `ping 192.168.123.161`
4. Set `UNIMAN_IFACE` to the interface name (for example `en7` or `eth0`).

## Working with Claude Code

Open the repo in Claude Code. `CLAUDE.md` has the rules Claude follows, and the most important one is that it never runs the real robot on its own. Useful commands:

- `/new-task <description or video URL>`: write a task spec and scaffold its sim
- `/sim-task <name>`: build or refine the sim and controller, then run validation

## Layout

```
uniman/        shared Python: config, safety limits, real-robot client, viewer
tasks/         one folder per task (TASK.md, scene XML, controller, results)
scripts/       setup and helper scripts
videos/        reference videos (git-ignored)
third_party/   cloned upstream repos (git-ignored)
```

## Upstream projects

- [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python): DDS SDK for the real robot
- [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco): MuJoCo simulator that speaks the SDK's low-level DDS topics
- [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym): RL locomotion training and sim2sim/sim2real deployment
- [mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie): robot models (`unitree_g1`, `unitree_h1`, `unitree_go2`)

## Safety

Humanoid robots are heavy and fast. Always run on a gantry or harness first, keep the remote e-stop in hand, and keep people out of the work area. Read [SAFETY.md](SAFETY.md) before running anything on hardware.

## License

MIT
