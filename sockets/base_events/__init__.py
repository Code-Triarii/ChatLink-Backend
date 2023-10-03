from config.logger import get_logger

def connect():
    get_logger().info(
        {
            'User connected'
        }
    )

def user_disconnect():
    get_logger().info(
        {
            'action': 'User Disconnected'
        }
    )