from random import randint
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/generate_password')
def GeneratePassword():
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", "{", "}", "|"]

    rand1 = randint(0, 25)
    rand2 = randint(0, 25)
    rand3 = randint(0, 8)
    rand4 = randint(0, 13)
    rand5 = randint(0, 25)
    rand6 = randint(0, 25)
    rand7 = randint(0, 8)
    rand8 = randint(0, 13)

    password = upper[rand1] + lower[rand2] + num[rand3] + special[rand4] + upper[rand5] + lower[rand6] + num[rand7] + special[rand8]

    return render_template('index.html', variable=password)


if __name__ == "__main__":
    app.run()
