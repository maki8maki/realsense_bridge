# realsense_bridge

ROS2のみに対応しているDepthカメラをROS1で使用するために[realsense-ros](https://github.com/IntelRealSense/realsense-ros)と[ros1_bridge](https://github.com/ros2/ros1_bridge)を起動するためのパッケージ

Ubuntu 20.04とD405の組み合わせのみで動作確認している

## Install

ワークスペースを作成し、レポジトリをクローンする

```bash
mkdir -p colcon_ws/src
cd ~/colcon_ws/src
git clone https://github.com/maki8maki/realsense_bridge.git
```

必要なパッケージをダウンロードする

```bash
cd ~/colcon_ws
vcs import src < src/realsense_bridge/realsense_bridge.repos
rosdep install -i --from-paths src/
```

ビルドする

```bash
colcon build --symlink-install --packages-skip ros1_bridge realsense_bridge
source install/local_setup.bash
colcon build --symlink-install --packages-select ros1_bridge realsense_bridge --cmake-force-configure
```

（ros1_bridgeのビルドは別に行ったほうが良いみたいなのでそれに準じている）

[realsense-ros](https://github.com/IntelRealSense/realsense-ros)や[ros1_bridge](https://github.com/ros2/ros1_bridge)のインストール・ビルドなどでエラー等が出た場合はそれぞれのレポジトリを参照する

## Usage

ターミナルA：ROS1の起動

```bash
source /opt/ros/<ros1_distro>/setup.bash
roscore
```
---

ターミナルB：realsense_bridgeの実行

```bash
source /opt/ros/<ros2_distro>/setup.bash
source ~/colcon_ws/install/local_setup.bash
ros2 launch realsense_bridge_launch.py
```

---

ターミナルC：ROS1でrealsenseを利用するコードの実行

```bash
source /opt/ros/<ros1_distro>/setup.bash
source ~/catkin_ws/devel/local_setup.bash
rosrun <package_name> <file_name>
```

