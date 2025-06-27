from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/ip")
def ipinfo():
    forwarded = request.headers.get("X-Forwarded-For", request.remote_addr)
    ip = forwarded.split(',')[0]  # falls es mehrere sind, nimm den ersten
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
    except:
        data = {"error": "API request failed"}

    return jsonify({
        "ip": ip,
        "country": data.get("country", "Unbekannt"),
        "city": data.get("city", "Unbekannt"),
        "isp": data.get("isp", "Unbekannt")
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
