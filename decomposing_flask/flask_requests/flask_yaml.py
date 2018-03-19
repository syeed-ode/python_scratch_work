from flask import Flask
import yaml  # requires PyYAML


app = Flask(__name__)


def yamlify(data, status=200, headers=None):
    """
        This function proves that a tuple can be returned by a
        view by being converted to a Response object by Flask.

        Typically the Flask expects a callable object that can
        recieve the 'environ' and 'start_response' arguments.

        :param data:
        :param status:
        :param headers:
        :return:
    """
    _headers = {'Content-Type': 'application/x-yaml'}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers


@app.route('/api')
def my_microservice():
    """
        The way Flask handles requests can be summarized as follows:
            1. When the application starts, any function decorated
               with @app.route() is registered as a view, and stored
               into the app.url_map.
            2. A call is dispatched to the right view depending on
               its endpoint and method.
            3. A Request object is created in a thread-safe
               thread-local execution context.
            4. A Response object wraps the content to send back.

        :return:
    """
    return yamlify(['Hello', 'YAML', 'World!'])


if __name__ == "__main__":
    app.run()