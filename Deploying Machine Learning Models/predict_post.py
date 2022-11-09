from crypt import methods
from distutils.log import debug
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

app = Flask('churn')

# use 'POST' because we want to send some information about customer
@app.route('/predict', methods=['POST'])
def predict():
    # request contains the information from request
    # get_json() reads the binary file (assumes that it is a JSON) and return a python dictionary
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    # our response is also a JSON, so we need to prepare it
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)





