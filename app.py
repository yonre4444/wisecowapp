from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Moo! Cows are amazing 🐄",
    "Wisdom comes slowly, like milk from a cow 🥛",
    "Keep calm and love cows ❤️",
    "Life is better with cows around 🌿"
]

@app.route("/")
def home():
    return f"<h2>{random.choice(quotes)}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
