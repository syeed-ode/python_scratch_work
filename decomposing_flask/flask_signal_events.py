from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available


if not signals_available:
    """
        Signal feature only works if install blinker
    """
    raise RuntimeError("pip install blinker")


app = Flask(__name__)


def finished(sender, response, **extra):
    print('About to send a response')
    print(response)


request_finished.connect(finished)


@app.route('/api')
def my_microservice():
    return jsonify({'Hello': 'World'})


if __name__ == "__main__":
    app.run()
