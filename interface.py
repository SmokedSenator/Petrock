from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/backdoors')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/shop')
def shop():
    return render_template("shop.html")

if __name__ == "interface":
    app.run(debug=True)