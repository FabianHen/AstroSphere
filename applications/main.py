from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

@app.route('/intern/events')
def intern_events():
    return render_template('intern_events.html')

@app.route('/intern/rooms')
def intern_rooms():
    return render_template('intern_rooms.html')

@app.route('/intern/planets')
def intern_planets():
    return render_template('intern_planets.html')

@app.route('/intern/telescopes')
def intern_telescopes():
    return render_template('intern_telescopes.html')

@app.route('/back_to_home')
def back_to_home():
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)
