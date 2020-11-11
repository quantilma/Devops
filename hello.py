from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Buenas tardes 11/11/20, son las 03:22 pm'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
