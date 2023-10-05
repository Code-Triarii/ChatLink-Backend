from flask_socketio import join_room, leave_room, send, emit

def on_join(data):
    join_room(data['room_id'])
    emit('receive_message', (data["user"],'', True), to=data['room_id'], include_self=False)
    
def on_leave(data):
    leave_room(data['room_id'])
    emit('receive_message', (data["user"],'', None), to=data['room_id'], include_self=False)