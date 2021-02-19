from gym.envs.registration import register

register(
    id='TestEnv-v0',
    entry_point='registration_test.env:TestEnv',
)
