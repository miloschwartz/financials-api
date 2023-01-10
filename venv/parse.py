import json
import data

# INCOME STATEMENT
def get_ebitda(income_stmt):
    ebitda = {}
    for year in income_stmt:
        ebitda[int(year['date'].split("-")[0])] = int(year['ebitda']) // 1000000 
    return ebitda

def get_revenue(income_stmt):
    revenue = {}
    for year in income_stmt:
        revenue[int(year['date'].split("-")[0])] = int(year['revenue']) // 1000000 
    return revenue

def get_net_income(income_stmt):
    net_income = {}
    for year in income_stmt:
        net_income[int(year['date'].split("-")[0])] = int(year['netIncome']) // 1000000 
    return net_income

# CASH FLOW STATEMENT
def get_free_cash_flow(cash_flow_stmt):
    free_cash_flow = {}
    for year in cash_flow_stmt:
        free_cash_flow[int(year['date'].split("-")[0])] = int(year['freeCashFlow']) // 1000000  
    return free_cash_flow

# BALANCE SHEET
def get_long_term_debt(balance_sheet):
    long_term_debt = {}
    for year in balance_sheet:
        long_term_debt[int(year['date'].split("-")[0])] = int(year['longTermDebt']) // 1000000  
    return long_term_debt

def get_cash(balance_sheet):
    cash = {}
    for year in balance_sheet:
        cash[int(year['date'].split("-")[0])] = int(year['cashAndCashEquivalents']) // 1000000  
    return cash

def get_profile(profile_sheet):
    profile = {}
    for key,value in profile_sheet[0].items():
        profile[key] = value
    return profile

def get_ratios(ratios_sheet):
    ratios = {}
    for key,value in ratios_sheet[0].items():
        ratios[key] = round(value, 2)
    return ratios

def get_financials(ticker):
    financials = {}
    income_stmt = data.load_income_stmt(ticker)
    cash_flow_stmt = data.load_cash_flow_stmt(ticker)
    balance_sheet = data.load_balance_sheet(ticker)
    financials['ebitda'] = get_ebitda(income_stmt)
    financials['revenue'] = get_revenue(income_stmt)
    financials['freeCashFlow'] = get_free_cash_flow(cash_flow_stmt)
    financials['longTermDebt'] = get_long_term_debt(balance_sheet)
    financials['netIncome'] = get_net_income(income_stmt)
    financials['cash'] = get_cash(balance_sheet)
    with open("financials.json", "w") as f:
        f.write(json.dumps(financials, indent=4))
    return json.dumps(financials, indent=4)