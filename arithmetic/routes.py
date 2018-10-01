from flask import request, Response
import arithmetic
from lib import predict, is_prime


@app.route('/api/predict')
def predict_handler():
    """Parse the argument of the request, intendedly a comma-separated list of values,
    evaluate the model, and format the response
    
    Returns
    -------
    str
        JSON list with the prediction
    """
    x = request.args.get('x')
    data = np.array(x.split(','), dtype=np.float64)
    prediction = predict(data)

    return make_json_response(prediction.tolist())
	
	
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/square')
def square():
    x = request.args.get('x')
    x = int(x)
    return f"The square of {x} is {x**2}"


@app.route('/cube')
def cube():
    x = request.args.get('x')
    x = int(x)
    return f"The cube of {x} is {x**3}"

@app.route('/name')
def name():
    x = request.args.get('name')
    return f"Hola {x}, tu nombre en mayusculas es {x.upper()}"


@app.route('/isPrime')
def checkPrime():
    if 'x' in request.args:
        x = request.args.get('x')
        n = int(x)
        return f'El número {n}' + (' no' if not is_prime(n) else '') + ' es primo!!'
    else:
        return 'Bad parameters in the request'
