---
description: Write a task spec (from a description or a video) and scaffold its sim
argument-hint: <task description or video URL/path>
---

Create a new uniman task from: $ARGUMENTS

1. Pick a short snake_case name and copy `tasks/_template/` to `tasks/<name>/`.
2. If a video was given, download it to `videos/` if needed, watch it closely, and write out the motion phases, the props and their approximate dimensions, and any timing you can observe.
3. Fill in `TASK.md`. The success criteria must be something `eval.py` can measure in sim.
4. Write `scene.xml`, which includes the robot from `third_party/mujoco_menagerie/unitree_<model>/` and adds the props, and check that it loads with mujoco.
5. Stop and show the user the spec before writing any controller.
