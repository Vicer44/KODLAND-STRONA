from flask import Flask, abort, render_template

app = Flask(__name__)


def result_calculate(size, lights, device):
    """Return a simple energy-use estimate in kWh."""
    return size * 100 + lights * 0.04 + device * 5


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:size>')
def lights(size):
    if size not in (1, 2, 3):
        abort(404)
    return render_template('lights.html', size=size)


@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    if size not in (1, 2, 3) or lights not in (1, 3, 7, 10):
        abort(404)
    return render_template('electronics.html', size=size, lights=lights)


@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    if size not in (1, 2, 3) or lights not in (1, 3, 7, 10) or device not in (4, 7, 10):
        abort(404)
    return render_template('end.html', result=result_calculate(size, lights, device))


if __name__ == '__main__':
    app.run(debug=True)
