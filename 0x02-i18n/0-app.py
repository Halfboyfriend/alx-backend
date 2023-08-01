from flask import Flask, flash, render_template, redirect, request


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)