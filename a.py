from flask import Flask


app = Flask(__name__)


@app.route('/just-do-it')
def main():
    return "Hello, World"

if __name__ == '__main__':
    app.run()
