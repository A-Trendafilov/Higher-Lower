import random

from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


def make_bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"

    return wrapper


@app.route("/")
@make_bold
def index():
    return (
        "<h1>Guess a number between 0 and 9!</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=460px />"
    )


@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return (
            "<h1 style='color:green'>You found me!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=460px />"
        )
    elif number > random_number:
        return (
            "<h1 style='color:blue'>Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=460px />"
        )
    elif number < random_number:
        return (
            "<h1 style='color:red'>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=460px />"
        )


if __name__ == "__main__":
    app.run(debug=True)
