from flask import Flask, jsonify, g, request


app = Flask(__name__)

@app.before_request
def authenticate():
    """
        This function acts as a preprocessing filter
        it demontstrates two fuctions:
        1. Flask's pre-refquest processing (filter)
        2. The ability to assign thread safe global
           variables, within a request context, using
           "g"

    :return:
    """
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anaonymous'


@app.route('/api')
def my_microservice():
    return jsonify({'Hello': g.user})


if __name__ == "__main__":
    app.run()
