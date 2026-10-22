---
description: Build or refine a task's controller in sim and run its evaluation
argument-hint: <task name>
---

Work on `tasks/$ARGUMENTS/` in simulation only.

1. Read `TASK.md` and any existing files in the folder.
2. Write or improve `controller.py`, starting with the simplest approach that could meet the success criteria.
3. Write or update `eval.py`. It runs headless over several randomized trials and writes `results/summary.json`, plus `results/best.mp4` when useful.
4. Run the eval and iterate until it passes or you're stuck. Report the numbers.
5. Once it passes, write `real.py` using `uniman.real` (safety-clamped) and give the user the command to run it. Do not run it yourself.
