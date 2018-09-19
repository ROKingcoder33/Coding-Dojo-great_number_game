from flask import Flask, render_template, session, request, redirect
import random
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    if 'number' in session:
        print(session)
        print('\n')
    else:
        session['number'] = random.randrange(0, 101)
        print('Random Number is: ', session['number'])
        print('\n')
    return render_template('index.html')


@app.route('/youGuessed', methods=['POST'])
def youGuessed():
    print(request.form)
    print('Vistor Guessed: ', request.form['chosenNum'])
    print('Random Number is: ', session['number'])
    print('\n')
    guessed = int(request.form['chosenNum'])
    if 'number in session':
        # If the guess is correct
        if guessed == session['number']:
            session['verdict'] = "Correct"
        # If the guess is high
        elif guessed > session['number']:
            session['verdict'] = "High"
        # If the guess is low
        elif guessed < session['number']:
            session['verdict'] = "Low"
        # else guess a number between 1 to 100
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
