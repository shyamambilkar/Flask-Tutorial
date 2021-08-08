from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder= 'templates')


@app.route('/')
def hello():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    return "Welcome %s"%name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['fname']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('fname')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
