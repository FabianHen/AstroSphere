import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
from databaseConnection import *

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

@app.route('/terminal/directions')
def directions():
    return render_template('directions.html')

@app.route('/terminal/shop/snacks', methods=['GET'])
def get_snacks():
    query_result = execute_sql_query_list_of_dicts("SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse "+
                                "FROM SNACK LEFT JOIN BESTAENDE_SNACK ON SNACK.id = BESTAENDE_SNACK.SNACK_id "+
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
                                "FROM MERCHARTIKEL LEFT JOIN BESTAENDE_MERCH ON MERCHARTIKEL.id = BESTAENDE_MERCH.MERCHARTIKEL_id "+
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
    try:
        data = request.json.get('id')
        procedure_result = execute_procedure_list_of_dicts("VERANSTALTUNG_MEDIUM_DETAILS", data)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")

@app.route('/intern/events/book_event', methods=['POST'])
def book_event():
    try:
        data = request.json
        params = [data['datum'], int(data['raum_id']), data['name'], data['beschreibung'], '[2]']

        print(params)
        procedure_result = execute_procedure("BUCHE_VERANSTALTUNG", params)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        
@app.route('/intern/events/book_medium', methods=['POST'])
def book_event_medium():
    try:
        data = request.json
        params = list(data.values())
        print(data)
        procedure_result = execute_procedure_list_of_dicts("BUCHE_VERANSTALTUNG_MEDIUM", params)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")

@app.route('/intern/events/allEvents', methods=['GET'])
def get_all_events():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG ORDER BY datum ASC")

@app.route('/intern/events/mineEvents', methods=['GET'])
def get_mine_events():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG WHERE id IN (SELECT veranstaltung_id FROM VERANSTALTUNG_ANGESTELLTER WHERE angestellter_id = 2) ORDER BY datum ASC")

@app.route('/intern/events/details', methods=['POST'])
def get_event_details():
    return execute_sql_query("SELECT * FROM VERANSTALTUNG WHERE datum > current_date")

@app.route('/intern/rooms')
def intern_rooms():
    return render_template('intern_rooms.html')

@app.route('/intern/rooms/roomlist', methods=['GET'])
def intern_roomlist():
    query_result = execute_sql_query_list_of_dicts("SELECT * FROM RAUM")
    return jsonify(query_result)

@app.route('/intern/rooms/freeRooms', methods=['GET'])
def intern_free_rooms():
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
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_RAUM_BEZEICHNUNG", bezeichnung)
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

@app.route('/intern/planets/planetsystemlist', methods=['GET'])
def intern_planetsystemlist():
    query_result=execute_sql_query("Select * from planetensysteme")
    return jsonify(query_result)

@app.route('/intern/planets/search_planetsystem_bezeichnung', methods=['POST'])
def get_planetsystem_by_bezeichnung():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_PLANETENSYSTEM_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/add_changes_planetsystem', methods=['POST'])
def add_changes_planetsystem():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['GALAXIE_ID']), data_objects['NAME'], data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("insert_into_planetensystem", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
@app.route('/intern/planets/save_changes_planetsystem', methods=['POST'])
def save_changes_planetsystem():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['GALAXIE_ID']), data_objects['NAME'], data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("update_into_planetensystem", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/planetlist', methods=['GET'])
def intern_planetlist():
    query_result=execute_sql_query("Select * from planeten")
    return jsonify(query_result)

@app.route('/intern/planets/search_planet_bezeichnung', methods=['POST'])
def get_planet_by_bezeichnung():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_PLANET_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/add_changes_planet', methods=['POST'])
def add_changes_planet():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['PLANETENSYSTEM_ID']), int(data_objects['ZENTRUMSPLANET_ID']), data_objects['NAME'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['UMLAUFZEIT_TAGE']), float(data_objects['TEMPERATUR_CELSIUS']), float(data_objects['FALLBESCHLEUNIGUNG']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("insert_into_planet", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/save_changes_planet', methods=['POST'])
def save_changes_planet():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['PLANETENSYSTEM_ID']), int(data_objects['ZENTRUMSPLANET_ID']), data_objects['NAME'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['UMLAUFZEIT_TAGE']), float(data_objects['TEMPERATUR_CELSIUS']), float(data_objects['FALLBESCHLEUNIGUNG']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("update_into_planet", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
@app.route('/intern/planets/starimagelist', methods=['GET'])
def intern_starimagelist():
    query_result=execute_sql_query("Select * from sternenbilder")
    return jsonify(query_result)

@app.route('/intern/planets/search_starimage_bezeichnung', methods=['POST'])
def get_starimage_by_bezeichnung():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_STERNENBILD_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/add_changes_starimage', methods=['POST'])
def add_changes_starimage():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [data_objects['NAME'], int(data_objects['ANZAHL_STERNE']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("insert_into_sternenbild", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
app.route('/intern/planets/save_changes_starimage', methods=['POST'])
def save_changes_starimage():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [data_objects['NAME'], int(data_objects['ANZAHL_STERNE']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("update_into_sternenbild", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/starlist', methods=['GET'])
def intern_starlist():
    query_result=execute_sql_query("Select * from sterne")
    return jsonify(query_result)

@app.route('/intern/planets/search_star_bezeichnung', methods=['POST'])
def get_star_by_bezeichnung():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_STERN_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/add_changes_star', methods=['POST'])
def add_changes_star():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['STERNENBILD_ID']), int(data_objects['PLANETENSYSTEM_ID']),data_objects['NAME'], data_objects['TYP'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['ENTFERNUNG_LJ']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("insert_into_stern", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
@app.route('/intern/planets/save_changes_star', methods=['POST'])
def save_changes_star():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['STERNENBILD_ID']), int(data_objects['PLANETENSYSTEM_ID']),data_objects['NAME'], data_objects['TYP'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['ENTFERNUNG_LJ']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("update_into_stern", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
 
@app.route('/intern/planets/cometlist', methods=['GET'])
def intern_cometlist():
    query_result=execute_sql_query("Select * from kometen")
    return jsonify(query_result)

@app.route('/intern/planets/search_comet_bezeichnung', methods=['POST'])
def get_comet_by_bezeichnung():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_KOMET_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/planets/add_changes_comet', methods=['POST'])
def add_changes_comet():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['GALAXIE_ID']), data_objects['NAME'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['UMLAUFZEIT_J']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("insert_into_komet", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
@app.route('/intern/planets/save_changes_comet', methods=['POST'])
def save_changes_comet():
    try:
        data_objects = request.json
        if not data_objects:
            return jsonify({"error": "No data provided"}), 400

        params = [int(data_objects['GALAXIE_ID']), data_objects['NAME'], float(data_objects['DURCHMESSER_KM']), float(data_objects['MASSE_KG']), float(data_objects['UMLAUFZEIT_J']), data_objects['INFORMATIONEN']]
        print(params)
        execute_procedure("update_into_komet", params)
        return jsonify(True)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500

@app.route('/intern/telescopes')
def intern_telescopes():
    return render_template('intern_telescopes.html')

@app.route('/intern/telescopes/telescopeList', methods=['GET'])
def telescope_list():
    query_result = execute_sql_query("SELECT * FROM TELESKOP")
    return jsonify(query_result)

@app.route('/intern/telescopes/search_telescope_by_name', methods=['POST'])
def teleskop_by_name():
    try:
        bezeichnung = request.json.get('bezeichnung')
        procedure_result = execute_procedure_list_of_dicts("SUCHE_TELESKOP_BEZEICHNUNG", bezeichnung)
        return jsonify(procedure_result)
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify(False), 500
    
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
                params=[newKunde['nachname'], newKunde['vorname'], newKunde['email'], newKunde['telefonnummer']]
                execute_procedure("new_customer", params)

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
                if int(databaseItem['SNACK_ID'])==int(shoppingItem[0]):
                    if databaseItem['BESTAND']==None:
                        available.append(False)
                    elif int(databaseItem['BESTAND']<int(shoppingItem[3])):
                        available.append(False)
                    else:
                        available.append(True)
                        print(int(databaseItem['BESTAND']))
                    if int(databaseItem['BESTAND'])<=10:
                        snack_id = str(databaseItem['SNACK_ID'])
                        quantity = str(7)
                        params = [databaseItem['SNACK_ID'], 7]
                        execute_procedure("nachbestellung_snack", params)
                        emailText = f"Nachbestellung von Merch\n ID: {merch_id}\n Anzahl: {quantity}"
                        #send_email(emailText)

        else:
            for databaseItem in itemNumMerch:

                if int(databaseItem['MERCHARTIKEL_ID'])==int(shoppingItem[0]):
                    if databaseItem['BESTAND']==None:
                        available.append(False)
                    elif int(databaseItem['BESTAND'])<int(shoppingItem[3]):
                        available.append(False)
                    else:
                        available.append(True)

                    if int(databaseItem['BESTAND']) <= 10:
                        params = [databaseItem['MERCHARTIKEL_ID'], 7]
                        print(params)
                        execute_procedure("nachbestellung_merch", params)

                    merch_id = str(databaseItem['MERCHARTIKEL_ID'])
                    quantity = str(7)
                    emailText = f"Nachbestellung von Merch\n ID: {merch_id}\n Anzahl: {quantity}"
                    #send_email(emailText)

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
                if 'Tag' in aktItem['type']:
                    params[0]="Tag"
                elif 'Monat' in aktItem['type']:
                    params[0]="Monat"
                else:
                    params[0]="Jahr"
                execute_procedure("VERKAUFEN_TICKET", params)
            elif int(aktItem['id'])%2==0:
                execute_procedure("VERKAUFEN_SNACK", params)
            else:
                execute_procedure("VERKAUFEN_MERCH", params)
        return True,OrderNum




def send_email(message):
    print("send Email: ", message)
    sender_email = "astrosphere.intern@gmail.com"
    receiver_email = "astrosphere.intern@gmail.com"
    password = "astrosphere!123"
    name = "AstroSphere"

    msg = MIMEMultipart()
    msg['From'] = f"{name} <{sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = "Shop Nachbestellung"

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("E-Mail erfolgreich gesendet!")

    server.quit()





if __name__ == '__main__':
    app.run(debug=True)
