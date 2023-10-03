from flask import Flask
from flask_socketio import SocketIO
from flask_restx import Api, Resource
from config import get_config
from sockets.base_events import connect, user_disconnect
from sockets.user_events.room import on_join, on_leave
from sockets.user_events.auth import sent_message, user_connection

config = get_config()

app = Flask(__name__)
app.config['SECRET_KEY'] = config['GENERAL']['COOKIE_SECRET']

#services
api = Api(app)
socketio = SocketIO(app)

socketio.on_event('connect', connect)
socketio.on_event('disconnect', user_disconnect)

socketio.on_event('join_chat_room', on_join)
socketio.on_event('leave_chat_room', on_leave)

socketio.on_event('user_connect', user_connection)
socketio.on_event('sent_message', sent_message)

@api.route('/test')
class index(Resource):
    def get(self):
        return {'title': 'chat', 'developed_by': 'CodeTriarii'}
    
if __name__ == '__main__':
    socketio.run(app, host=config["GENERAL"]["HOST"], port=int(config["GENERAL"]["PORT"]))