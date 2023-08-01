from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def home():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)