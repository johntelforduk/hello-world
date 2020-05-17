# Hello world web-service.

from flask import Flask
from datetime import datetime
import socket


def now_str() -> str:
    """Return the time right now as a nicely formatted string."""
    time_list = str(datetime.now()).split('.')
    return time_list[0]


app = Flask(__name__)


# Homepage.
@app.route("/", methods=['GET'])
def home():
    return ('Hello from flask...'
            + '<br><br>The time right now is: ' + now_str()
            + '<br><br>The hostname is: ' + socket.gethostname())


if __name__ == "__main__":
    app.run()
