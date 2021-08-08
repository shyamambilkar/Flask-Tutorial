from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return "Welcome to Data Science class"


@app.route('/hello/<name>')
def my_Function(name):
    return 'Welcome %s Data Science Class' % name


@app.route('/blog/<int:blog_id>')
def my_blog(blog_id):
    return 'Blod Id Number is %d' % blog_id


if __name__ == "__main__":
    app.run(debug=True)
