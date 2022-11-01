from crypt import methods
from distutils.log import debug
from flask import Flask

app = Flask('ping')

@app.route('/ping', methods=['GET'])
def pong():
    return "PONG"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)