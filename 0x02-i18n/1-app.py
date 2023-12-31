from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

babel = Babel(app)
app.config.from_object(Config)



@app.route('/')
def home():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)