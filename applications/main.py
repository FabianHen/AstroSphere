from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

@app.route('/terminal/shop')
def shop():
    return render_template('shop.html')

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

@app.route('/send_data', methods=['POST'])
def send_data():
    try:
        action = request.json.get('action')
        data = request.json.get('data')

        result = False

        if action == "checkAvailableItems":
            result=check_data(data)
        elif action == "buyShoppingCart":
            if check_data(data):
                result=buyShoppingCart(data)
            else:
                result=False

        return jsonify(success=result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(success=False), 500


def check_data(data):
    available=[]
    for item in data['shoppingCart']:
        #check ob das item: type anzahl-mal in der Datenbank verfügbar ist

        x = random.random()
        if x<0.8:
            available.append(True)
        else:
            available.append(False)
    return available

def buyShoppingCart(data):
    #send items to Database and reduce item number
    buySuccessful=False
    if buySuccessful:
        return True
    else:
        return False





if __name__ == '__main__':
    app.run(debug=True)
