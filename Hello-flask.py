from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center; color: black;">Hello world!</h1>'

@app.route('/bye')
def bye():
    return "<em><b>ok, Bye</b></em>"

@app.route('/hello/<name>/<int:num>')
def greet(name, num):
    return f'<em><b>Hello, {name}, you are {num} years old!</b></em>'


if __name__ == "__main__":
    app.run(debug=True)
