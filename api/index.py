import os

from flask import (
    Flask,
    render_template,
    request
)
from sqlalchemy import SQLAlchemy

from .utils import add_up


app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
