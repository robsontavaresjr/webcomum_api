import os

from flask_api import FlaskAPI
import pandas as pd


app = FlaskAPI(__name__)


@app.route('/')
def example():
    return {'hello': 'world'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
