import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16

import serial
import time




class publisher(Node):

    def __init__(self):
        super().__init__('arduino_wraper')
        self.serial = serial.Serial("/dev/ttyACM0", 9600)
        time.sleep(1)

        self.pub_a = self.create_publisher(Int16, 'value_a', 10)
        self.pub_b = self.create_publisher(Int16, 'value_b', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.subscription = self.create_subscription(Int16, 'write', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        val = msg.data
        payload_send = str(int(val)) + ","
        self.serial.write(str.encode(payload_send))
        #print(payload_send)
        

    def timer_callback(self):
        
        payload_rec = self.serial.readline()
        a = int(chr(payload_rec[0]))
        b1 = payload_rec[2]; b2 = payload_rec[3]; b3 = payload_rec[4]
        b = int(chr(b1) + chr(b2) + chr(b3))
        #print(a)

        msg_a = Int16()
        msg_b = Int16()
        msg_a.data =  a
        msg_b.data =  b
        self.pub_a.publish(msg_a)
        self.pub_b.publish(msg_b)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = publisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

