from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    logs = []
    if request.method == "POST":
        logs = request.form.get("logs").splitlines()
        payload = {"log": logs}
        try:
            response = requests.post("http://llm_service:5000/analyze", json=payload)
            result = response.json()
        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result, logs="\n".join(logs))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
