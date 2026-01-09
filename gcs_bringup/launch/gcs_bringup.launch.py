from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('tank_bringup'),
        'config',
        'uart_config.yaml'
    )

    config_cam = os.path.join(
        get_package_share_directory('tank_bringup'),
        'config',
        'camera_config.yaml'
    )

    return LaunchDescription([
        Node(
            package='gcs_pkg',
            executable='hub_node',
        ),
    ])