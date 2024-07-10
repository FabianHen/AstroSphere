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
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM GET_SNACK_DRINKS")
    return jsonify(query_result)
@app.route('/terminal/shop/snacks/sweet', methods=['GET'])
def get_sweet():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM GET_SNACK_SWEET")
    return jsonify(query_result)
@app.route('/terminal/shop/snacks/salty', methods=['GET'])
def get_salty():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM GET_SNACK_SALTY")
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
    return jsonify(query_result)

@app.route('/terminal/shop/merch/clothing', methods=['GET'])
def get_clothing():
    query_result= execute_sql_query_list_of_dicts("SELECT * FROM GET_MERCH_CLOTHING")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/accessoires', methods=['GET'])
def get_accessoires():
    query_result= execute_sql_query_list_of_dicts("SELECT * FROM GET_MERCH_ACCESSOIRES")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/householdItem', methods=['GET'])
def get_householdItem():
    query_result= execute_sql_query_list_of_dicts("SELECT * FROM GET_MERCH_HOUSEHOLDITEM")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/stationery', methods=['GET'])
def get_stationery():
    query_result= execute_sql_query_list_of_dicts("SELECT * FROM GET_MERCH_STATIONERY")
    return jsonify(query_result)

@app.route('/terminal/shop/merch/other', methods=['GET'])
def get_other():
    query_result= execute_sql_query_list_of_dicts("SELECT * FROM GET_MERCH_OTHER")
    return jsonify(query_result)

@app.route('/terminal/shop/tickets', methods=['GET'])
def get_tickets():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM TICKETSTUFE")
    return jsonify(query_result)

@app.route('/terminal/shop/events/day', methods=['GET'])
def get_events_day():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG_TAG ")
     
@app.route('/terminal/shop/events/month', methods=['GET'])
def get_events_month():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG_MONAT ")
   

@app.route('/terminal/shop/events/year', methods=['GET'])
def get_events_year():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG_JAHR ")

@app.route('/intern/events')
def intern_events():
    return render_template('intern_events.html')

@app.route('/intern/events/medien', methods=['GET'])
def get_medien():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM MEDIUM_VIEW")
    return jsonify(query_result)

@app.route('/intern/events/medium', methods=['POST'])
def get_medium():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM MEDIUM_VIEW ")
    return jsonify(query_result)

@app.route('/intern/events/allEvents', methods=['GET'])
def get_all_events():
    query_result = execute_sql_query_list_of_dicts("SELECT id, raum_id, name, datum FROM VERANSTALTUNG WHERE datum > current_date")
    return jsonify(query_result)

@app.route('/intern/events/details', methods=['POST'])
def get_event_details():
    query_result = execute_sql_query_list_of_dicts("SELECT id, raum_id, name, datum FROM VERANSTALTUNG")
    return jsonify(query_result)

@app.route('/intern/rooms')
def intern_rooms():
    return render_template('intern_rooms.html')

@app.route('/intern/rooms/roomlist', methods=['GET'])
def intern_roomlist():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM FREIE_RAEUME")
    return jsonify(query_result)

@app.route('/intern/rooms/search_room_capacity', methods=['POST'])
def get_room_by_capacity():
    try:
        capacity = request.json.get('capacity')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_RAUM_KAPAZITAET", capacity)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
   

@app.route('/intern/rooms/search_room_bezeichnung', methods=['POST'])
def get_room_by_bezeichnung():
    try:
        bezecihnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_RAUM_BEZEICHNUNG", bezecihnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/rooms/search_free_rooms', methods=['POST'])
def get_room_by_date():
    try:
        date = request.json.get('date')
        procedure_result = execute_procedure_list_of_dicts("GET_FREIE_RAUME_DATUM", date)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")

@app.route('/intern/planets')
def intern_planets():
    return render_template('intern_planets.html')

@app.route('/intern/planets/planetlist', methods=['GET'])
def intern_planetlist():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM PLANETEN")
    return jsonify(query_result)

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
        newKunde = request.json.get('kunde')

        result = False

        if action == "checkAvailableItems":
            result=check_data(data)
        elif action == "buyShoppingCart":
            result=[buyShoppingCart(data)]
            if newKunde!=None:
                params=[newKunde['vorname'], newKunde['nachname'], newKunde['email'], newKunde['telefonnummer']]
                #execute_procedure("NEUER_KUNDE", params)

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
        itemName=str(shoppingItem[1])
        if "Ticket" in itemName:
            available.append(True)
        elif int(shoppingItem[0])%2==0:
            for databaseItem in itemNumSnack:
                if int(databaseItem[0])==int(shoppingItem[0]):
                    if databaseItem[3]==None:
                        available.append(False)
                    elif int(databaseItem[3]<int(shoppingItem[3])):
                        available.append(False)
                    else:
                        available.append(True)
                    if int(databaseItem[3])<10:
                        print("Nachbestellen von: ", databaseItem[1])
                        #nachbestellen vom aktuellen Snack
                        params=[int(databaseItem[3]), 10]
                        #execute_procedure("ORDER_SNACK", params)

        else:
            for databaseItem in itemNumMerch:
                if int(databaseItem[0])==int(shoppingItem[0]):
                    if databaseItem[3]==None:
                        available.append(False)
                    elif int(databaseItem[3])<int(shoppingItem[3]):
                        available.append(False)
                    else:
                        available.append(True)
                    if int(databaseItem[3])<10:
                        print("Nachbestellen von: ", databaseItem[1])
                        #nachbestellen von Merch
                        params=[int(databaseItem[3]), 10]
                        #execute_procedure("ORDER_MERCH", params)
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
            if "Ticket" in aktItem['type']:
                print("update Database with ticket")
                #execute_procedure("VERKAUFEN_TICKET", params)
            elif int(aktItem['id'])%2==0:
                print("update Database with snack")
                #execute_procedure("VERKAUFEN_SNACK", params)
            else:
                print("update Database with merch")
                #execute_procedure("VERKAUFEN_MERCH", params)
        return True,OrderNum


if __name__ == '__main__':
    app.run(debug=True)
