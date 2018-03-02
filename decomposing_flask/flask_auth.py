from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def auth() -> None:
    """ This function demonstrates Flask's ability to
        authomatically decomponse an authorization header
        To see it execuate a curl statement as such

        curl http://localhost:5000/ -u tarek:password
    """
    print("The raw Auhtorization header")
    print(request.environ["HTTP_AUTHORIZATION"])
    print("Flask's Authorization header")
    print(request.authorization)
    return ""


if __name__ == "__main__":
    app.run()
