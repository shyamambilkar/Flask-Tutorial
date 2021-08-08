from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Welcome to Flask Framework'


@app.route('/main')
def Hello1():
    return 'Welcome to Data Science'


if __name__ == "__main__":
    app.run(debug=True)
