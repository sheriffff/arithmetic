import numpy as np

def is_prime(n):
	return False
	
	
def predict(x: np.array):
    """Predict for the input values using the trained model
    
    Parameters
    ----------
    x : np.array
        Parsed input array of values
    
    Returns
    -------
    np.array
        Array of values with the predicted values
    """

    return 1 / (1 + np.exp(-(1.5046 * x - 4.0777)))

	
def make_json_response(value):
    """Build a JSON response that is vulnerable to X-Site scripting
    Good for RESTful API testing
    
    Parameters
    ----------
    value : Anything JSON serializable
        Value to be returned
    
    Returns
    -------
    flask.Response
        A response for the Flask app.
    """
    response = Response(json.dumps(value))

    # We can learn more about Access Control here: 
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    # It is a protection about cross-site scripting
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = "text/javascript charset=utf-8"
    return response