from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
@app.route('/index/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/result/')
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
