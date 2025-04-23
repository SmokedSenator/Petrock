from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Welcome to the starters"

if __name__ == "interface":
    app.run(debug=True)