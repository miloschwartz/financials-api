import urllib.request
import json
import config
import os

API_KEY = config.API_KEY


def load_income_stmt(ticker):
    income_stmt = {}
    path = "income_stmts/" + ticker + "_income_stmt.json"
    if os.path.exists(path) is False:
        print(path + " is NOT cached. Fetching data from api.")
        url = "https://financialmodelingprep.com/api/v3/income-statement/" + \
            ticker + "?limit=120&apikey=" + API_KEY
        response = urllib.request.urlopen(url)
        income_stmt = json.loads(response.read())
        with open(path, "w") as f:
            f.write(json.dumps(income_stmt, indent=4))
    else:
        print(path + " already cached.")
        with open(path) as f:
            income_stmt = json.load(f)
    return income_stmt


def load_cash_flow_stmt(ticker):
    cash_flow_stmt = {}
    path = "cash_flow_stmts/" + ticker + "_cash_flow_stmt.json"
    if os.path.exists(path) is False:
        print(path + " is NOT cached. Fetching data from api.")
        url = "https://financialmodelingprep.com/api/v3/cash-flow-statement/" + \
            ticker + "?limit=120&apikey=" + API_KEY
        response = urllib.request.urlopen(url)
        cash_flow_stmt = json.loads(response.read())
        with open(path, "w") as f:
            f.write(json.dumps(cash_flow_stmt, indent=4))
    else:
        print(path + " already cached.")
        with open(path) as f:
            cash_flow_stmt = json.load(f)
    return cash_flow_stmt


def load_balance_sheet(ticker):
    balance_sheet = {}
    path = "balance_sheets/" + ticker + "_balance_sheet.json"
    if os.path.exists(path) is False:
        print(path + " is NOT cached. Fetching data from api.")
        url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/" + \
            ticker + "?limit=120&apikey=" + API_KEY
        response = urllib.request.urlopen(url)
        balance_sheet = json.loads(response.read())
        with open(path, "w") as f:
            f.write(json.dumps(balance_sheet, indent=4))
    else:
        print(path + " already cached.")
        with open(path) as f:
            balance_sheet = json.load(f)
    return balance_sheet

def load_ratios(ticker):
    ratios = {}
    path = "ratios/" + ticker + "_ratios.json"
    if os.path.exists(path) is False:
        print(path + " is NOT cached. Fetching data from api.")
        url = "https://financialmodelingprep.com/api/v3/ratios-ttm/" + \
            ticker + "?apikey=" + API_KEY
        response = urllib.request.urlopen(url)
        ratios = json.loads(response.read())
        with open(path, "w") as f:
            f.write(json.dumps(ratios, indent=4))
    else:
        print(path + " already cached.")
        with open(path) as f:
            ratios = json.load(f)
    return ratios

def load_profile(ticker):
    profile = {}
    path = "profile/" + ticker + "_profile.json"
    if os.path.exists(path) is False:
        print(path + " is NOT cached. Fetching data from api.")
        url = "https://financialmodelingprep.com/api/v3/profile/" + \
            ticker + "?apikey=" + API_KEY
        response = urllib.request.urlopen(url)
        profile = json.loads(response.read())
        with open(path, "w") as f:
            f.write(json.dumps(profile, indent=4))
    else:
        print(path + " already cached.")
        with open(path) as f:
            profile = json.load(f)
    return profile