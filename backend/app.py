from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app) 

# Dummy audio transcription and text simplification data
transcription_data = ['そうですか。<ruby>呼吸<rt>こきゅう</rt></ruby><ruby>困難<rt>こんなん</rt></ruby>の<ruby>自覚<rt>じかく</rt></ruby><ruby>症状<rt>しょうじょう</rt></ruby>があるんですね。','そうですね。<ruby>頻脈<rt>ひんみゃく</rt></ruby>や<ruby>動悸<rt>どうき</rt></ruby>はありますか？']
simplified_data = ['そうですか。<ruby>息苦<rt>いきぐる</rt></ruby>しいんですね。いつからですか？','そうですね。<ruby>心臓<rt>しんぞう</rt></ruby>が<ruby>ドキドキ<rt></rt></ruby>することはありますか？']

@socketio.on('transcription')
def handle_hello(data):
    dummy_index = data['message']
    message = transcription_data[dummy_index%2]
    emit('transcription', {'message': message})

@socketio.on('simplification')
def handle_hello(data):
    dummy_index = data['message']
    message = simplified_data[dummy_index%2]
    emit('simplification', {'message': message})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5010)