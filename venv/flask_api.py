from flask import Flask
from flask_cors import CORS
import parse

app = Flask(__name__)
CORS(app)

@app.route("/get-financials/<ticker>")
def show_financials(ticker):
    return parse.get_financials(str(ticker))

app.run(host="0.0.0.0", port=80)