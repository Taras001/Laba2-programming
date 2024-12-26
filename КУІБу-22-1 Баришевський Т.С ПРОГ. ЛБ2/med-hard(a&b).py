import requests
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
def get_usd_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for currency in data:
                if currency['cc'] == 'USD':
                    formatted_date = datetime.strptime(date, "%Y%m%d").strftime("%d.%m.%Y")
                    return {
                        "currency": currency['cc'],
                        "rate": currency['rate'],
                        "date": formatted_date
                    }
    except Exception:
        pass
    return None

@app.route("/currency", methods=["GET"])
def get_currency():
    param = request.args.get('param')
    if param == "today" or param == "yesterday":
        if param == "today":
            date = datetime.now().strftime("%Y%m%d")
        elif param == "yesterday":
            date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
        
        usd_rate = get_usd_rate(date)
        if usd_rate:
            return jsonify(usd_rate)
    return "", 204 
if __name__ == "__main__":
    app.run(port=1234)