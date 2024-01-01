from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)



