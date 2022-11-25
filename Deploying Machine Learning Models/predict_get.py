from crypt import methods
from distutils.log import debug
from flask import Flask

# give a name
app = Flask('ping-pong')

# decorator is a way to add some extra functionality to our function and
# it allows us to make it a web service.
# define the address and method
@app.route('/ping', methods=['GET'])
def pong():
    return "PONG"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)