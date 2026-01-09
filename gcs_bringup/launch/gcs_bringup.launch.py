from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    config_joy = os.path.join(
        get_package_share_directory('gcs_bringup'),
        'config',
        'trustmaster.yaml'
    )

    return LaunchDescription([
        
        Node(
            package='joy',
            executable='joy_node',
        ),

        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name = 'teleop_node',
            parameters=[config_joy],
        ),

        Node(
            package='gcs_pkg',
            executable='hud_node',
        )
    ])