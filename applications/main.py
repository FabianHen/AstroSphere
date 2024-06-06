from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

@app.route('/intern')
def intern():
    return render_template('intern.html')

@app.route('/back_to_home')
def back_to_home():
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)
