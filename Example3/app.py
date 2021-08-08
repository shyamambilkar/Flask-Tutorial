from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def employee():
    return render_template('employee.html')


@app.route('/result', methods=['POST', 'GET'])
def employee_result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
