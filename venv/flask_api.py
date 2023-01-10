from flask import Flask
from flask_cors import CORS
import parse
import data

app = Flask(__name__)
CORS(app)

@app.route("/get-financials/<ticker>")
def show_financials(ticker):
    return parse.get_financials(str(ticker))

@app.route("/get-ratios/<ticker>")
def show_ratios(ticker):
    ratios_sheet = data.load_ratios(str(ticker))
    return parse.get_ratios(ratios_sheet)

@app.route("/get-profile/<ticker>")
def show_profile(ticker):
    profile_sheet = data.load_profile(str(ticker))
    return parse.get_profile(profile_sheet)

app.run(host="0.0.0.0", port=80)