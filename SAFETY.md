# Safety checklist for the real robot

Check every item before each hardware session.

- [ ] The task passed its sim success criteria (`tasks/<name>/results/`)
- [ ] The robot is on a gantry or harness for the first run of any new task
- [ ] The operator holds the remote and knows the damping / e-stop combo
- [ ] The area is clear of people, pets and anything fragile, with at least 2 m around the robot
- [ ] The battery is charged and the joints are at normal temperature
- [ ] Velocity and joint limits in `uniman/safety.py` are not raised for this task
- [ ] Someone else knows a hardware test is happening

If anything looks wrong, damp the robot first and investigate afterwards.
