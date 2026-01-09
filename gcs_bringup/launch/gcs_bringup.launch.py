from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    config_teleop = os.path.join(
            get_package_share_directory('my_robot_teleop'),
            'config',
            'trustmaster.yaml'
    )

    return LaunchDescription([
        
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            parameters=[config_teleop]
        ),

        Node(
            package='gcs_pkg',
            executable='hub_node',
        )
    ])