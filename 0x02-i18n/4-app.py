from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
   
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')

       
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template('4-index.html', home_title=home_title, home_header=home_header)

if __name__ == '__main__':
    app.run(debug=True)
