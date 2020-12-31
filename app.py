from flask import Flask,jsonify
from random import choice

app = Flask(__name__)


@app.route('/')
def home():
    responses=["hi","hello","how are you ?","good to see you here"]
    response = [
        {'id':0 ,'message': choice(responses),'trigger':1},
                ]
    return jsonify(response)


if __name__ == '__main__':
    app.run()
