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
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse "+
                                "FROM SNACK LEFT JOIN BESTAENDE_SNACK ON SNACK.id = BESTAENDE_SNACK.id "+
                                "WHERE BESTAENDE_SNACK.BESTAND > 0 "+
                                "ORDER BY SNACK.id")
    #for testing with every item
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse FROM SNACK ")
    return jsonify(query_result)

@app.route('/terminal/shop/snacks/drinks', methods=['GET'])
def get_drinks():
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse FROM SNACK WHERE bezeichnung LIKE '%Coke%' OR bezeichnung LIKE '%IceTea%' OR bezeichnung LIKE '%Beer%' OR bezeichnung LIKE '%Sprite%'")
    return jsonify(query_result)
@app.route('/terminal/shop/snacks/sweet', methods=['GET'])
def get_sweet():
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse FROM SNACK WHERE bezeichnung LIKE '%Sugar%' OR bezeichnung LIKE '%Gummi%' OR bezeichnung LIKE '%Sweet%' OR beschreibung LIKE '%süß%' OR beschreibung LIKE '%Zucker%'")
    return jsonify(query_result)
@app.route('/terminal/shop/snacks/salty', methods=['GET'])
def get_salty():
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse FROM SNACK WHERE beschreibung LIKE '%chips%' OR beschreibung LIKE '%salz%' OR beschreibung LIKE '%würzig%'")
    return jsonify(query_result)






    
@app.route('/terminal/shop/merch', methods=['GET'])
def get_merch():
    query_result = execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse " +
                                "FROM MERCHARTIKEL LEFT JOIN BESTAENDE_MERCH ON MERCHARTIKEL.id = BESTAENDE_MERCH.id "+
                                "WHERE BESTAENDE_MERCH.BESTAND > 0 "+
                                "GROUP BY MERCHARTIKEL.groesse, MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung "+
                                "ORDER BY MERCHARTIKEL.groesse")
    #for testing with every item
    query_result = execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL")
    print(query_result)
    return jsonify(query_result)

@app.route('/terminal/shop/merch/clothing', methods=['GET'])
def get_clothing():
    query_result= execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL WHERE bezeichnung LIKE '%Hoodie%' OR bezeichnung LIKE '%Shirt%' OR bezeichnung LIKE '%Sock%' OR bezeichnung LIKE '%Vest%'")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/accessoires', methods=['GET'])
def get_accessoires():
    query_result= execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL WHERE beschreibung LIKE '%brille%' OR beschreibung LIKE '%Magnet%' OR beschreibung LIKE '%Stick%'")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/householdItem', methods=['GET'])
def get_householdItem():
    query_result= execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL WHERE beschreibung LIKE '%tasse%' OR beschreibung LIKE '%vase%' OR beschreibung LIKE '%set%'")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/stationery', methods=['GET'])
def get_stationery():
    query_result= execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL WHERE beschreibung LIKE '%Skizze%'")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/other', methods=['GET'])
def get_other():
    query_result= execute_sql_query_list_of_dicts("SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse FROM MERCHARTIKEL WHERE beschreibung LIKE '%schirm%'")
    return jsonify(query_result)





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
    itemNumMerch=execute_sql_query("SELECT * from BESTAENDE_MERCH")
    itemNumSnack=execute_sql_query("SELECT * from BESTAENDE_SNACK")


    for aktItem in data['shoppingCart']:
        shoppingCartItems.append((aktItem['id'], aktItem['type'], aktItem['größe'], aktItem['anzahl']))


    for shoppingItem in shoppingCartItems:
        if int(shoppingItem[0])%2==0:
            for databaseItem in itemNumSnack:
                if int(databaseItem[0])==int(shoppingItem[0]):
                    if databaseItem[3]==None:
                        available.append(False)
                    elif int(databaseItem[3]<int(shoppingItem[3])):
                        available.append(False)
                    else:
                        available.append(True)
        
        else:
            for databaseItem in itemNumMerch:
                if int(databaseItem[0])==int(shoppingItem[0]):
                    if databaseItem[3]==None:
                        available.append(False)
                    elif int(databaseItem[3])<int(shoppingItem[3]):
                        available.append(False)
                    else:
                        available.append(True)

    return available

OrderNum=0
def buyShoppingCart(data):
    global OrderNum
    available=check_data(data)

    if False in available:
        return False,0
    else:
        OrderNum+=1
        if OrderNum>9999:
            OrderNum=0
        for aktItem in data['shoppingCart']:
            params=[int(aktItem['id']), int(aktItem['anzahl'])]
            if int(aktItem['id'])%2==0:
                print("update Database with snack")
                #execute_procedure("VERKAUFEN_SNACK", params)
            else:
                print("update Database with merch")
                #execute_procedure("VERKAUFEN_MERCH", params)
        return True,OrderNum


if __name__ == '__main__':
    app.run(debug=True)
