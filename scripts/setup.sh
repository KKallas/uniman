#!/usr/bin/env bash
# Clone upstream robot models, simulator and RL repos into third_party/ (shallow).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p third_party

clone() {
  local url=$1 dir=third_party/$2
  if [ -d "$dir" ]; then
    echo "✓ $2 (exists)"
  else
    git clone --depth 1 "$url" "$dir"
  fi
}

clone https://github.com/google-deepmind/mujoco_menagerie.git mujoco_menagerie
clone https://github.com/unitreerobotics/unitree_mujoco.git unitree_mujoco
clone https://github.com/unitreerobotics/unitree_rl_gym.git unitree_rl_gym
clone https://github.com/unitreerobotics/unitree_sdk2_python.git unitree_sdk2_python

echo "done. try: uv run python -m uniman.view --headless"
