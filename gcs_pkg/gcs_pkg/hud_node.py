import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class TankGcsNode(Node):
    def __init__(self):
        super().__init__('video_hud')
        self.sub = self.create_subscription(Image, '/camera/image_raw', self.cb, 10)
        self.bridge = CvBridge()

        self.battery_status = 50

    def cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg)
        cv2.putText(frame, "Battery: "+ self.battery_status +"%", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.imshow("HUD", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = TankGcsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()