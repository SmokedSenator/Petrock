from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the starters"


@app.route('/about')
def about():
    return "All rights are NOT reserved"

if __name__ == "interface":
    app.run(debug=True)