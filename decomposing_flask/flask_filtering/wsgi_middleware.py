"""
     This module demonstrates the ability to extend Flask to
     provide enhanced or alternate functionality. This module
     utilizes WSGI middleware by wrapping the calls made to
     WSGI endpoints. We are extending WSGI apps here.

     This middleware is useful in a testing environment.
"""
from flask import Flask, jsonify, request
import json


class XFFMiddleware(object):
    def __init__(self, app, real_ip='10.1.1.1'):
        self.app = app
        self.real_ip = real_ip

    def __call__(self, environ, start_response):
        """
            This middleware fakes the 'HTTP_X_FORWARDED_FOR'
            header so that Flask thinks it's behind a proxy.

            It assures the header is not already set.

            Flask uses the incoming WSGI environment data to
            create the request object (PYMsDEv58).

            :param environ:
            :param start_response:
            :return:
        """
        if 'HTTP_X_FORWARDED_FOR' not in environ:
            values = '%s, 10.3.4.5, 127.0.0.1' % self.real_ip
            environ['HTTP_X_FORWARDED_FOR'] = values
        return self.app(environ, start_response)

app = Flask(__name__)

# Notice we wrap the WSGI app. In Flask the app object
# is not the WSGI application itself as we've seen earlier
app.wsgi_app = XFFMiddleware(app.wsgi_app)


@app.route('/api')
def my_microservice():
    """
        Whent the application tries to get the remote IP
        address, this method assure the application behaves
        properly.

        The remote_addr will get the IP of the proxy and not
        the real client.

        ####################################################
        ###              CAUTION     CAUTION             ###
        ###That text was lifted from the book. I don't have
        ###confidence in what this logic is doing. I'm not
        ###100% sure of it's applicability.
        ####################################################

        The overall point here is valid however: You can intercept
        and augment request data by overriding the WSGI application
        (as shown here) or by intercepting signals (module:
        flask_signal_events) or by utilizing filters (module:
        flask_request_filter).

        :return:
    """
    if "X-Forwarded-For" in request.headers:
        ips = [forip.strip() for forip in request.headers['X-Forwarded-For'].split(',')]
        ip = ips[0]
    else:
        ip = request.remote_addr
    return jsonify({"Hello": ip})


if __name__ == "__main__":
    app.run()
