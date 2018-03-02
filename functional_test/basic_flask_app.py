from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError


class RegisteredUser(BaseConverter):
    """ This subclass of werkzeug """
    def to_python(self, value):
        print("\n\nin RegisteredUser.to_python with value: " + value)
        if value in _USERS:
            print("in RegisteredUser.to_python with _USERS[value]: " + _USERS[value])
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
print("Prior to setting RegisteredUser with app.url_map.converters: ")
print(app.url_map.converters)
app.url_map.converters['registered'] = RegisteredUser
print("\nAfter to setting RegisteredUser with app.url_map.converters: ")
print(app.url_map.converters)

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}


@app.route('/api')
def my_microservice():
    print("Here is the request:")
    print(request)
    print("\nHere is the environment:")
    print(request.environ)
    print("\nHere is the response")
    response = jsonify({'Hello': 'World!'})
    print(response)
    print("\nHere is the response data")
    print(response.data)
    return response


@app.route('/api/person/<registered:name>')
def person(name):
    print("\nin person name: ")
    print(name)
    print()
    print("in person with app.url_map")
    print(app.url_map)
    response = jsonify({'Hello hey': name})
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run()
