from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    data = {
        "currency": "USD",
        "rate": "41.5"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=1234)