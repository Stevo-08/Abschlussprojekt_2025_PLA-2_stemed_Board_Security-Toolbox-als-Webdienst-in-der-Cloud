from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url")
    try:
        r = requests.get(url, timeout=5)
        return jsonify(dict(r.headers))
    except Exception as e:
        return jsonify({"Fehler": str(e)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)
app.run(host="127.0.0.1", port=5050)
