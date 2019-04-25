from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/ssafy')
def ssafy():
    return 'Hi, ssafy'


@app.route('/hi/<string:name>')
def hi(name):
    return f'hi {name}!'


@app.route('/pick_lotto')
def pick_lotto():
    return jsonify(random.sample(range(1, 46), 6))


@app.route('/dictionary/<string:word>')
def dictionary(word):
    my_words = {'apple': '사과'}
    if word in my_words:
        result = f'{word}은(는) {my_words[word]}!'
    else:
        result = f'{word}은(는) 나만의 단어장에 없는 단어입니다!'
    return result


if __name__ == '__main__':
    print('__name__ is __main__')
    app.run(debug=True)
else:
    print('unknown')


# export FLASK_ENV='development'
