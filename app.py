from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

FOLLOW_UPS = [
    {
        "q": "Aww 💞 When should we go out?",
        "options": ["This weekend 🌷", "Tonight 🌙", "Soon please 🥹"]
    },
    {
        "q": "What sounds perfect for our date?",
        "options": ["Coffee ☕", "Dinner 🍝", "Long walk 🌆"]
    },
    {
        "q": "Final question: Will you let me spoil you with love? ❤️",
        "options": ["Yes, always 😘", "Absolutely 💕", "100% yes 💗"]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/no-message")
def no_message():
    msg = random.choice([
        "Really? 🙃",
        "Think again 😘",
        "No is disabled 😌",
        "Try Yes maybe? 💘"
    ])
    return jsonify({"message": msg})

@app.route("/api/followups")
def followups():
    return jsonify(FOLLOW_UPS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
