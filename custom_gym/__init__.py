from __future__ import absolute_import
from gymnasium.envs.registration import register

# Mujoco
# --------------------------------------------------

register(
    id='CustomHumanoid-v1',
    entry_point='custom_gym.envs.mujoco:HumanoidEnv',
    max_episode_steps=50,
)

register(
    id='CustomHumanoid-v2',
    entry_point='custom_gym.envs.mujoco:HumanoidEnv',
    max_episode_steps=1000,
)

register(
    id='CustomHumanoidStandup-v1',
    entry_point='custom_gym.envs.mujoco:HumanoidStandupEnv',
    max_episode_steps=50,
)

register(
    id='CustomHumanoidStandup-v2',
    entry_point='custom_gym.envs.mujoco:HumanoidStandupEnv',
    max_episode_steps=1000,
)

register(
    id='CustomPendulum-v1',
    entry_point='custom_gym.envs.classic_control:PendulumEnv',
    max_episode_steps=50,
)

register(
    id='CustomReacher-v1',
    entry_point='custom_gym.envs.mujoco:ReacherEnv',
    max_episode_steps=50,
    reward_threshold=-3.75,
)

register(
    id='CustomPusher-v1',
    entry_point='custom_gym.envs.mujoco:PusherEnv',
    max_episode_steps=50,
    reward_threshold=0.0,
)
