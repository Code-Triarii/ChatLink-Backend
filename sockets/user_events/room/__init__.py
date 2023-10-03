from flask_socketio import join_room, leave_room, send

def on_join(data):
    if(data['room_id'] == ''):
        data['room_id'] = 'default_room'
    join_room(data['room_id'])
    send(f'{data["user"]} has joined to room {data["room_id"]}', to=data['room_id'], broadcast=True, include_self=False)
    
def on_leave(data):
    leave_room(data['room_id'])
    send(f'{data["user"]} has left room {data["room_id"]}', to=data['room_id'])