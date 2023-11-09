from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173'])

@app.route('/')
def hello_world():
    return {"status":200,"ping":[51,23,44,332,999]}

if __name__ == '__main__':
    app.run()