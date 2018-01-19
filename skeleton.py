from flask import (Flask, render_template)

app = Flask(__name__)


@app.route('/')
def skeleton():
    return render_template('skeleton.html')


if __name__ == '__main__':
    app.run()
