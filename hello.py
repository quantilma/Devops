from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return 'Buenos dias equipo gente Quantil'
=======
    return 'Buenos dias. Hoy es 13-11-2020.'
>>>>>>> 67ed3bb8fe5c2fb34c887c0364ea346465af08dd

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
