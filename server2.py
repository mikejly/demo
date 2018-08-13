#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from flask_socketio import join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client_event')
def client_msg(msg):
    print(msg)
    emit('server_response', {'data': msg['data']})
    
@socketio.on('connect_success')
def connected_msg(msg):

    emit('server_response', {'data': msg['data']})
'''
@socketio.on('join')
def on_join(data):
    uername=data['username']
    room=data['room']
    join_room(room)
    send(username + ' has entered the room.',room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)
'''

if __name__ == '__main__':
    socketio.run(app,debug=True,host='0.0.0.0',port=5000)
    #5000的端口有何特殊之处？