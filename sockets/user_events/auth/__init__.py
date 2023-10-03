from flask_socketio import send
from config.logger import get_logger

def user_connection(data):
    get_logger().info(
        {
            'user': data['user'],
            'action': 'Connected'
        }
    )
    send(f'You are connected as {data["user"]}')