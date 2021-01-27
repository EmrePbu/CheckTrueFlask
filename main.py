from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    _number = dict()
    _number['on'] = '10'
    _number['yirmi'] = '20'
    return render_template('index.html', number=_number)


if __name__ == '__main__':
    app.run(debug=True)
