from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/typograf', methods=['POST'])
def typograf():
    text = request.form['text']
    return text.upper()


if __name__ == "__main__":
    app.run()
