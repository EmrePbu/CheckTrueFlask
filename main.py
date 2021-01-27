from flask import Flask, render_template

app = Flask(__name__)


# main page route
@app.route('/')
def index():
    numbers = [1, 2, 3, 4, 5]
    return render_template('index.html', numbers=numbers)


# doc page
@app.route('/doc')
def documentation():
    return render_template('documentation.html')


# register page
@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
