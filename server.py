from flask import Flask, render_template, request
from typo import typo

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/typograf', methods=['POST'])
def typograf():
    text = typo(request.form['text'])
    return text


if __name__ == "__main__":
    app.run(debug=True)
