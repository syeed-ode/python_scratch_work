from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions


def JsonApp(app):
    """
        The JsonApp function wraps a Flask app instance, and sets up
        the custom JSON error handler for every 4xx and 50x error that
        might occur.

        :param app:
        :return:
    """
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {'code': error.code, 'description': error.description, 'message': str(error)}
        else:
            description = "Sorry abort mapping isn't an object available on tis function"  # abort.mapping[500].description
            result = {'code': 500, 'description': description, 'message': str(error)}

        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    return app

app = JsonApp(Flask(__name__))

@app.route('/api')
def my_microservice():
    a = 100
    print("I want to execute over this application.")
    print(a)
    raise TypeError("Some Exception")


if __name__ == '__main__':
    app.run(debug=True)
