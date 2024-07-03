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

@app.route('/terminal/shop/snacks', methods=['GET'])
def get_snacks():
    try:
        query_result = execute_sql_query("SELECT SNACK.id, SNACK.bezeichnung, SNACK.verkauf_preis_kg " +
                                   "FROM BESTAENDE_SNACK LEFT JOIN SNACK ON BESTAENDE_SNACK.id = SNACK.id " +
                                   "WHERE BESTAENDE_SNACK.BESTAND > 0" +
                                   "ORDER BY SNACK.id")
        if query_result is not None:
            result = calc_snack_price(query_result)
        print(result)

        return jsonify(success=result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(success=False), 500
    
@app.route('/terminal/shop/merch', methods=['GET'])
def get_merch():
    try:
        
        return jsonify(success=True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(success=False), 500

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
            result=[buyShoppingCart(data)]

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
    
    for shoppingItem in shoppingCartItems:
        for databaseItem in ItemNumbersInDatabase:
            if int(databaseItem[0])==int(shoppingItem[0]):
                if databaseItem[3]==None:
                    available.append(False)
                elif int(databaseItem[3])<int(shoppingItem[3]):
                    available.append(False)
                else:
                    available.append(True)

    return available

OrderNum=9998
def buyShoppingCart(data):
    global OrderNum
    available=check_data(data)

    if False in available:
        return False,0
    else:
        OrderNum+=1
        if OrderNum>9999:
            OrderNum=0
        for aktItem in data:
            if aktItem['id']%2!=0:
                sqlCommand="BEGIN VERKAUFEN_SNACK("+aktItem['id']+", "+aktItem['anzahl']+"); END;"
                execute_sql_query(sqlCommand)
                pass
            else:
                sqlCommand="BEGIN VERKAUFEN_MERCH("+aktItem['id']+", "+aktItem['anzahl']+"); END;"
                execute_sql_query(sqlCommand)
        return True,OrderNum


def calc_snack_price(data):
    nacho_weight = 0.1
    popcorn_weight = 0.075
    salad_weight = 0.15
    chips_weight = 0.1
    gummi_bears_weight = 0.15
    bottle_volume = 0.33

    for snack in data:
        if snack[1].find('Nachos') != -1:
            snack[2] = snack[2]*nacho_weight
        elif snack[1].find('Popcorn') != -1:
            snack[2] = snack[2]*popcorn_weight
        elif snack[1].find('Salad') != -1:
            snack[2] = snack[2]*salad_weight
        elif snack[1].find('Chips') != -1:
            snack[2] = snack[2]*chips_weight
        elif snack[1].find('Gummi Bears') != -1:
            snack[2] = snack[2]*gummi_bears_weight
        elif (snack[1].find('Coke') != -1) or (snack[1].find('Sprite') != -1) or (snack[1].find('IceTea') != -1) or (snack[1].find('Beer') != -1):
            snack[2] = snack[2]*bottle_volume
    
    return data
            

if __name__ == '__main__':
    app.run(debug=True)
