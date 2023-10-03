from config.logger import get_logger
from flask_socketio import emit

def sent_message(data):
    get_logger().info(
        'message'
    )
    emit(
        'receive_message', 
        (data['user'], data['message']),
        broadcast=True,
        include_self=False
        )