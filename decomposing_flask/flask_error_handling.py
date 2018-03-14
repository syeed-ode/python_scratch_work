"""
    This module holds two decorated functions which 1)
    represents a Flask view and 2) error handler.
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(500)
def error_handling(error):
    """
        This decorated function catches all error types
        and returns the error message as a string. This
        occurs only when Flask returns a 500 error.

        However, in case your application issues an HTTP
        404 or any other 4xx or 5xx response, you will
        be back to the default HTML responses that Flask
        sends.

        To handle specific errors see 

        :param error:
        :return:
    """
    return jsonify({'Error': str(error)}, 500)


@app.route('/api')
def my_microservice():
    raise TypeError("Some Exception")


if __name__ == "__main__":
    app.run()