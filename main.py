from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Моя сторінка на Flask 1</h1>"
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return "<h2>Про мене:</h2><p>Учень 7-го класу ЗОШ №111</p>"


# Лише для локального сервера
if __name__ == '__main__':
    app.run(debug=True)
