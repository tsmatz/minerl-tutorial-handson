import gym
import minerl.env.core
import minerl.env.comms
import numpy as np
from minerl.env.core import MineRLEnv
from collections import OrderedDict

class MyActionSpace(gym.spaces.Dict):
    def __init__(self):
        super().__init__(spaces={
            "move": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32)
        })

    def no_op(self):
        action = OrderedDict() 
        action['move'] = 0
        action['camera'] = [0, 0]
        return action

class MyObservationSpace(gym.spaces.Dict):
    def __init__(self):
        super().__init__(spaces={
            'pov': gym.spaces.Box(low=0, high=255, shape=(84, 84, 3), dtype=np.uint8),
        })

    def no_op(self):
        action = OrderedDict() 
        action['pov'] = np.zeros(shape=(84, 84, 3)).astype(int)
        return action

class MyEnvSpec:
    def __init__(self):
        self._action_space = MyActionSpace()
        self._observation_space = MyObservationSpace()

    @property
    def action_space(self):
        return self._action_space

    @property
    def observation_space(self):
        return self._observation_space

class TestEnv(MineRLEnv):
    def __init__(self):
        xml = "./lava_maze_minerl.xml"
        super().__init__(
            xml,
            MyObservationSpace(),
            MyActionSpace(),
            MyEnvSpec()
        )
