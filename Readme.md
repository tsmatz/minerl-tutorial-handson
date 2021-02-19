# MineRL Tutorial

This is step-by-step hands-on learning how MineRL work for beginners.<br>
(This is used in [Reinforcement Learning Day 2021](https://dllab.connpass.com/event/198873/) Hands-On in Deep Learning Lab community.)

## 1. Setup prerequisite environment

First, prepare your own machine.<br>
**Do not use low-spec machine**, since the training worker will request enough resources.<br>
Here we assume Ubuntu 18.04 on Standard D3 v2 with 4 cores and 14 GB RAM in Microsoft Azure.

Login to your machine.<br>
Make sure that python 3 is installed in your machine. (If not, please install Python 3.x.)

```
python3 -V
```

Install ```pip```.

```
sudo apt-get update
sudo apt-get -y install python3-pip
sudo -H pip3 install --upgrade pip
```

MineRL requires a monitor (screen), such as VNC, to run Minecraft.    
Then, install and start service for X remote desktop.

```
sudo apt-get update
sudo apt-get install lxde -y
sudo apt-get install xrdp -y
/etc/init.d/xrdp start  # password is required
```

> Use a virtual monitor (such as, ```xvfb```) instead, when you run training as a batch in background. (Here we use a real monitor for debugging.)

Allow inbound port 3389 (remote desktop protocol) for this computer in network setting.

> You can also use SSH tunnel (port 22) instead.

Restart your computer.

Finally, install Java runtime and set ```JAVA_HOME```, since it runs on Minecraft java edition (with mods).

```
sudo apt-get install openjdk-8-jdk
echo -e "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
source ~/.bashrc
```

## 2. Install MineRL

```
pip3 install minerl==0.3.6
```

## 3. Run your first agent

Login to computer **with remote desktop client** (please use a monitor) and clone this repository.

```
git clone https://github.com/tsmatz/minerl-hack.git
cd minerl-hack
```

Let's run a script (```test.py```) as follows. This script will start a custom mission (```lava_maze_minerl.xml```)<br>
In this environment, the agent will turn round 360 degree and then move forward by 1 step. (The agent might dive into lava and die.)

```
python3 test.py
```

## 4. Try step by step to the goal !

Next we'll run using python console.

Before starting, please change ```test.py``` and make an agent not to move forward.

Start python console as follows.

```
python3
```

Read and run a script (```test.py```) as follows.

```
exec(open('test.py').read())
```

Try to make an agent reach to a goal block (a blue lapis block) within 5 minutes. (Since the mission finishes in 5 minutes.)<br>
During each steps, make sure that the reward is correctly returned.

```
action = env.action_space.no_op()
action['move'] = 1
obs, reward, done, info = env.step(action)
```

![Game in this mission](https://tsmatz.files.wordpress.com/2021/01/20200717_minerl_missionfile.jpg)

## 5. Register and run your custom environment

For competition use, your own custom environments can be registered in Gym framework and all participants can start mission with Gym-integrated convenient manners.<br>
In this repository, the above mission has already been setup for environment's registration in ```registration_test``` folder. In this tutorial, let's start and run this custom mission.

First, run python console as follows.

```
python3
```

In the console, let's start our custom environment named ```TestEnv-v0```, which is registered in Gym framework.

```
import gym
import registration_test
env = gym.make('TestEnv-v0')
obs = env.reset()
```

Try to make an agent reach to a goal block within 5 minutes.

```
action = env.action_space.no_op()
action['camera'] = [0, 90]
obs, reward, done, info = env.step(action)
```

## 6. Run the built-in environments

In this tutorial, run one of the built-in environments in MineRL.<br>
Here we run the mission to search and obtain diamonds.

Run python console as follows.

```
python3
```

In the console, start the built-in mission ```MineRLObtainDiamond-v0```.

```
import gym
import minerl
env = gym.make('MineRLObtainDiamond-v0')
obs = env.reset()
```

Let's make your agent move as follows.<br>
For the specification of this mission (such as rewards, etc), see [here](https://minerl.io/docs/environments/index.html#minerlobtaindiamond-v0).

```
action = env.action_space.noop()
action['forward'] = 1
obs, reward, done, info = env.step(action)
```

## 7. Run training with reinforcement learning

After you have completed this tutorial, please go to "[Reinforcement Learning for MineRL Sample](https://github.com/tsmatz/minerl-maze-sample)" (next step).

<blockquote>
When your application cannot detect your display (monitor), please ensure to set "DISPLAY" as follows.<br>
(The error message "MineRL could not detect a X Server, Monitor, or Virtual Monitor" will show up.)

```
# check your display id
ps -aux | grep vnc
# set display id (when your display id is 10)
export DISPLAY=:10
```

When you cannot directly show outputs in your physical monitor, please divert outputs through a virtual monitor (xvfb).<br>
For instance, the following will show outputs (Minecraft game) on your own VNC viewer window through a virtual monitor (xvfb).

```
# install components
sudo apt-get install xvfb
sudo apt-get install x11vnc
sudo apt-get install xtightvncviewer
# generate xvfb monitor (99) and bypass to real monitor (10)
/usr/bin/Xvfb :99 -screen 0 768x1024x24 &
/usr/bin/x11vnc -rfbport 5902 -forever -display :99 &
DISPLAY=:10 /usr/bin/vncviewer localhost:5902 &
# run program
export DISPLAY=:99
python3 test.py
```
</blockquote>
