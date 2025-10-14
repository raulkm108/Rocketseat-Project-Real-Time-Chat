from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/chat', methods=['POST'])
def generate_chat():
    

if __name__ == '__main__':
    socketio.run(app,debug=True)