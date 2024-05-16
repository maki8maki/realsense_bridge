import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    launch_dir = get_package_share_directory("realsense2_camera")
    rs_launch = IncludeLaunchDescription(
        launch_description_source=os.path.join(launch_dir, "launch", "rs_launch.py"),
        launch_arguments={
            "align_depth.enable": "true",
            "enable_sync": "true",
            "enable_color": "true",
            "enable_depth": "true",
        }.items(),
    )

    bridge_node = Node(package="ros1_bridge", executable="dynamic_bridge", arguments=["--bridge-all-topics"])

    ld.add_action(rs_launch)
    ld.add_action(bridge_node)

    return ld
