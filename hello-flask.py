# Hello world web-service.

from flask import Flask

app = Flask(__name__)


# Homepage.
@app.route("/", methods=['GET'])
def home():
    return 'Hello from flask...'


if __name__ == "__main__":
    app.run()
