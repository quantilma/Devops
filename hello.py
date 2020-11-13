from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Buenos dias. Hoy es 13-11-2020.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
