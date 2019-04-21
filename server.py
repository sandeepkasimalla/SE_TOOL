
from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import subprocess
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yalamanchili Engineers'
socketio = SocketIO(app)

@socketio.on('my event')
def handle_my_custom_event(cmd):
    os.system(str(cmd))
    #subprocess.call(str(cmd),shell=True)
    print('received data: ' + str(cmd))

if __name__ == '__main__':
    socketio.run(app)


