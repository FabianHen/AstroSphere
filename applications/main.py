from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
from databaseConnection import *

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

@app.route('/shop/buyOrCheck', methods=['POST'])
def buyOrCheck():
    try:
        action = request.json.get('action')
        data = request.json.get('data')

        result = False

        if action == "checkAvailableItems":
            result=check_data(data)
        elif action == "buyShoppingCart":
            result=buyShoppingCart(data)

        return jsonify(success=result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(success=False), 500


def check_data(data):
    available=[]
    shoppingCartItems=[]
    ItemNumbersInDatabase=execute_sql_query("SELECT * from BESTAENDE_MERCH")

    for aktItem in data['shoppingCart']:
        shoppingCartItems.append((aktItem['id'], aktItem['type'], aktItem['größe'], aktItem['anzahl']))
    
    for databaseItem in ItemNumbersInDatabase:
        for shoppingItem in shoppingCartItems:
            if databaseItem[0]==shoppingItem[0]:
                if databaseItem[3]==None:
                    available.append(False)
                elif databaseItem[3]<shoppingItem[3]:
                    available.append(False)
                else:
                    available.append(True)

    return available

def buyShoppingCart(data):
    available=check_data(data)

    if False in available:
        return False
    else:
        #send items to Database and reduce item number
        return True





if __name__ == '__main__':
    app.run(debug=True)
