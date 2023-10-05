import socketio

from config import get_config

sio = socketio.Client()
config = get_config()

def chat_print(msg):
    print(f'CodeTriarii Chat: {msg}')

def join_chat_room(data):
    sio.emit('join_chat_room', data)
    chat_print(f'You have successfully logged in to the room: {data["room_id"]}')
    chat_print('Chat session started')
@sio.event
def joined_chat_room(data):
    chat_print(f'Now you are in the room {data["room_id"]}')

def user_connection():
    provided_user = input('Welcome to CodeTriarii Chat, What is your name?: ')
    chat_room = input(f'Nice to see you here, {provided_user}.\nWhich room do you want to join today?: ')

    data = {
        'user': provided_user,
        'room_id': chat_room
    }

    sio.emit('user_connect', {
        'user': str(provided_user)
    })

    join_chat_room(data)

    return data

@sio.on('receive_message')
<<<<<<< HEAD
def receive_message(user, message, join=False):
    if(join):
        print(f'User {user} joined to the chat room.')
    elif(join is False):
        print(f'Message received by {user} {message}')
    else:
        print(f'User {user} left the chat room.')
=======
def receive_message(user, message):
    print(f'Message received by {user} {message}')

>>>>>>> 97b3cc4f379a5ce3259500aa81157dd3acdd60ae
@sio.event
def send_message(user, message, room_id):
    sio.emit('sent_message', {'user': str(user), 'message': str(message), 'room_id': str(room_id)})
    print(f'Message sent: {message}')

@sio.event
def disconnect():
    chat_print('Disconnected.')

sio.connect(f'ws://{config["GENERAL"]["HOST"]}:{config["GENERAL"]["PORT"]}', wait_timeout=10)

user_data = user_connection()

exit = False

while(not exit):
    user_input = input()
    if(user_input == '/exit'):
        exit = True
        break
    send_message(user_data['user'], user_input, user_data['room_id'])

sio.disconnect()