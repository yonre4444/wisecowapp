from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "wisecowapp devops traaine",
]

@app.route("/")
def home():
    return f"<h2>{random.choice(quotes)}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
