from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
class Config:
    LANGUAGES = ['en', 'fr']

babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale ():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    locale = get_locale()
    return render_template('2-index.html', loc=locale)


if __name__ == '__main__':
    app.run(debug=True)