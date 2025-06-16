from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    total = 10
    occupied = random.sample(range(1, total + 1), 5)
    slots = [{"id": i, "status": "Occupied" if i in occupied else "Available"} for i in range(1, total + 1)]
    return render_template("index.html", slots=slots)

if __name__ == '__main__':
    app.run(debug=True)
