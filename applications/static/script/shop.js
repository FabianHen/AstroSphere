// SLEEPTIMER + DISPLAYTIMER = Gesamtzeit bis reset
const IDLETIMER = 50000;
const SLEEPTIMER = 10000;
// Colors for the Fade of the sleeptimer display
const STARTCOLOR = { r: 66, g: 4, b: 176 };
const ENDCOLOR = { r: 211, g: 13, b: 164 };

/**
 * Sends the user back to the main page of the Terminal
 */
function goBack() {
    window.location.href = window.location.href.split('/', window.location.href.split('/').length - 1).join('/');
}

/**
 * Collapses the given filter if its already unfolded. Switches to a display of all items of this filter and unfolds further filters if not.
 * Shows all tickets if filter is ticket_filter
 * @param {*} filter the filter that has been clicked (`"snack_filter"`, `"ticket_filter"`  or `"merch_filter"`)
 */
function collapseFilter(filter) {
    if (filter) {
        clearInterval(event_day_timer)
        clearInterval(event_month_timer)
        clearInterval(event_year_timer)
        if (filter == 'ticket_filter') {
            getTickets();
            return;
        }
        let content = document.getElementById(filter);
        if (content) {
            if (content.style.display == 'flex') {
                content.style.display = 'none';
                history.replaceState(null, '', document.location.origin + document.location.pathname);
            } else {
                // document.getElementsByClassName('filter_content').forEach(f => { f.style.display = 'none'; });
                content.style.display = 'flex';
                history.replaceState(null, '', `?selected=${filter}`);
                switch (filter) {
                    case 'snack_filter':
                        getSnacks('all');
                        break;
                    case 'merch_filter':
                        getMerch('all');
                        break;
                    default:
                        break;
                }
            }
        }
    }
}

let idle_timeout;
let sleep_timeout;

/**
 * Resets the idle timer and the sleep timer, if it has already started
 */
function resetTimers() {
    let sleepDiv = document.getElementById("sleepTimer")
    if (sleepDiv && sleepDiv.style.display == "flex") {
        sleepDiv.style.display = "none";
        clearTimeout(sleep_timeout);
        document.getElementById("timer").innerHTML = 10
    }
    clearTimeout(idle_timeout);
    idle_timeout = setTimeout(sleepTimer, IDLETIMER);
}

/**
 * Opens the sleeptimer window and updates the time that's left every second. The color of the displayed time is gradually changed from blue to pink. 
 * The user will be sent back to the main page if the timer runs out
 */
function sleepTimer() {
    clearTimeout(idle_timeout);
    let rounds_total = SLEEPTIMER / 1000;
    let current_round = rounds_total;
    document.getElementById("sleepTimer").style.display = "flex";
    sleep_timeout = setInterval(function () {
        current_round--;
        const factor = 1 - (current_round / rounds_total);
        const interpolatedColor = interpolateColor(STARTCOLOR, ENDCOLOR, factor);
        document.getElementById("timer").style.color = rgbToHex(interpolatedColor.r, interpolatedColor.g, interpolatedColor.b);
        document.getElementById("timer").innerHTML = current_round
        if (current_round < 0) {
            clearInterval(sleep_timeout);
            document.getElementById("sleepTimer").style.display = "none";
            goBack()
        }
    }, 1000);
}

/**
 * Converts a rgb values to a Hexcode
 * @returns a Hexcode that represents the given RGB values
 */
function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
}

/**
 * Calculates a Color between two given colors based on the given factor
 * @param {*} color1 the startcolor
 * @param {*} color2 the endcolor
 * @param {*} factor a factor between 0 and 1 to calculate the new color 
 * @returns a color between color1 and color 2
 */
function interpolateColor(color1, color2, factor) {
    const result = {
        r: Math.round(color1.r + factor * (color2.r - color1.r)),
        g: Math.round(color1.g + factor * (color2.g - color1.g)),
        b: Math.round(color1.b + factor * (color2.b - color1.b))
    };
    return result;
}

/**
 * Resets the timers and opens the Drop down filters of the previously selected category
 */
window.addEventListener("load", function (e) {
    let params = new URL(document.location).searchParams;
    let selected = params.get("selected");
    if (selected) {
        collapseFilter(selected);
    }
    // Timers will be reset when the user either moves the mouse or clicks on the screen
    document.addEventListener('mousemove', resetTimers);
    document.addEventListener('click', resetTimers);
    resetTimers();
});


shoppingCart = [];
var numberOfItems = 0;

class Artikel {
    constructor(id, type, beschreibung, größe, preis, anzahl, imagePath) {
        this.id = id;
        this.type = type;
        this.beschreibung = beschreibung;
        this.größe = größe;
        this.preis = preis;
        this.anzahl = anzahl;
        this.image = imagePath;
    }
}

class Kunde {
    constructor(vorname, nachname, email, telefonnummer) {
        this.vorname = vorname;
        this.nachname = nachname;
        this.email = email;
        this.telefonnummer = telefonnummer;
    }
}

/**
 * Adds an item to the shopping cart. If this Item has been added to the shoppingcart previously, 
 * the amount of this item will be increased
 */
function addItemToCart(id, type, beschreibung, größe, preis, anzahl, imagePath) {
    aktItem = new Artikel(id, type, beschreibung, größe, preis, anzahl, imagePath);
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type == aktItem.type && item.größe == aktItem.größe) {
            item.anzahl += aktItem.anzahl;
            numberOfItems += aktItem.anzahl;
            createItems();
            return;
        }
    }
    numberOfItems += aktItem.anzahl;
    shoppingCart.push(aktItem);
    createItems();
    var cart_badge = document.querySelector('.cart_badge');
    cart_badge.style.display = 'flex';
    cart_badge.innerHTML = shoppingCart.length;
}

/**
 * Removes a given item from the cart and updates the cart badge 
 * @param {} type the type of the item
 * @param {*} größe the size of the item
 * @param {*} num the amount to be removed
 */
function removeItemFromCart(type, größe, num) {
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type === type && item.größe == größe) {
            item.anzahl - num;
            if (item.anzahl <= 0) {
                shoppingCart.splice(i, 1);
            }
            var cart_badge = document.querySelector('.cart_badge');
            cart_badge.innerHTML = shoppingCart.length;
            if (shoppingCart.length == 0) {
                cart_badge.style.display = 'none';
            }
            return;
        }
    }
    console.log(`Artikel ${type} nicht gefunden.`);
}

/**
 * Creates HTML Items for all elements in the shoppingcart and adds them to the shoppingcart window
 */
function createItems() {
    var newHTMLString = "";
    for (let i = 0; i < shoppingCart.length; i++) {
        var newHTMLItem = "<div class='item' id='item_" + i + "'>\n";
        newHTMLItem += "\t<div style='height: 100%; width: 100%;'>\n";
        newHTMLItem += "\t\t<img src='"
        newHTMLItem += shoppingCart[i].image;
        newHTMLItem += "' alt='item image' id='item_" + i + "Img'>\n";
        newHTMLItem += "\t\t<h3 id='item_" + i + "Name'>" + shoppingCart[i].type + "</h3>\n";
        newHTMLItem += "\t\t<div class='line'></div>\n";
        newHTMLItem += "\t\t<p class='beschreibung' id='item_" + i + "Desc'><b>Beschreibung</b><br>" + shoppingCart[i].beschreibung + "</p>\n";
        if (shoppingCart[i].größe != "") {
            newHTMLItem += "\t\t<p class='groesse' id='item_" + i + "Gr'>Größe: " + shoppingCart[i].größe + "</p>\n";
        }
        newHTMLItem += "\t\t<p class='preis' id='item_" + i + "Preis'>Preis: " + shoppingCart[i].preis + "</p>\n";
        newHTMLItem += "\t\t<input type='number' min='0' max='10' value='" + shoppingCart[i].anzahl + "'  class='numberOfItems' placeholder='Menge: 1' id='item_" + i + "Num' onchange='updateShoppingCart(true)'>\n";
        newHTMLItem += "\t\t<img src='../static/images/trashcan_bold.svg' alt='delete' class='delete' onclick='deleteItem(" + i + ")' width='25' height='25'>\n"
        newHTMLItem += "\t\t<p class='Lager' id='item_" + i + "L' style='display: none;'>Auf Lager</p>\n";
        newHTMLItem += "\t\t<p class='nLager' id='item_" + i + "nL' style='display: none;'>Nicht Auf Lager</p>\n";
        newHTMLItem += "\t</div>\n</div>";

        newHTMLString += newHTMLItem + "\n\n";

    }

    document.getElementById('itemList').innerHTML = newHTMLString;
}

/**
 * Updates the displayed amount of each item and the displayed price of the order, checks for availability of products 
 * @param {boolean} updateNum if set, this function will check the amount of each item and will remove it if 0
 */
function updateShoppingCart(updateNum) {
    var gesSumme = 0.0;
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        const itemID = "item_" + i;
        const itemNumId = itemID + "Num";

        if (updateNum == true) {
            item.anzahl = document.getElementById(itemNumId).value;
            if (item.anzahl <= 0) {
                removeItemFromCart(item.type, item.größe, item.anzahl);
            }
        }

        document.getElementById(itemID + 'Num').value = item.anzahl;

        if (!(item.anzahl * item.preis <= 0)) {
            gesSumme += item.anzahl * item.preis;
        }
    }
    createItems();
    checkIfAvailable();
    document.getElementById('gesKostenNum').textContent = gesSumme.toFixed(2) + "€";
    var cart_badge = document.querySelector('.cart_badge');
    cart_badge.innerHTML = shoppingCart.length;
    if (shoppingCart.length == 0) {
        cart_badge.style.display = 'none';
    }
}

/**
 * Removes the item with the given id from the shoppingcart
 * @param {number} id 
 */
function deleteItem(id) {
    const aktItem = "item_" + id + "Num";
    document.getElementById(aktItem).value = 0;
    updateShoppingCart(true);
}

/**
 * Displays the order and its id based on the items in the shoppingcart
 */
function showOrder() {
    var htmlList = "";
    var price = 0;
    for (let i = 0; i < shoppingCart.length; i++) {
        const aktItem = shoppingCart[i];
        if (aktItem.anzahl > 0) {
            htmlList += "<div class='boughtItem'>\n\t";
            htmlList += "<p>" + aktItem.type + "</p>\n\t";
            if (aktItem.größe == null) {
                htmlList += "<p>-</p>\n\t";
            }
            else {
                htmlList += "<p>" + aktItem.größe + "</p>\n\t";
            }
            htmlList += "<p>" + aktItem.anzahl + "</p>\n\t";
            htmlList += "<p>" + aktItem.preis + "</p>\n\t";
            htmlList += "</div>\n";
            price += aktItem.anzahl * aktItem.preis;
        }
    }
    htmlList += "\n\t<div id='boughtItemPrice'>\n\t<p>gesamt Preis: " + price.toFixed(2) + "€</p>\n</div>";
    document.getElementById('listboughtItems').innerHTML = htmlList;
    document.getElementById('buyItems').style.display = "block";
}

/**
 * Opens the shoppingcart window if it is currently open. Closes it otherwise
 */
function goTo_shoppingCart() {
    if (document.getElementById('shoppingCart').style.display == "flex") {
        document.getElementById('shoppingCart').style.display = "none";
    }
    else {
        document.getElementById('shoppingCart').style.display = "flex";
    }
    updateShoppingCart(false);
}

/**
 * Resets order form and clears the shoppingcart
 */
function cancel_Order() {
    shoppingCart = [];
    updateShoppingCart();
    document.getElementById('shoppingCart').style.display = "none";
    document.getElementById('payment-form').reset();
    document.getElementById('personalInfoForm').reset();
}

/**
 * Closes the window that is used for collecting user information
 */
function cancelUserInput() {
    document.getElementById('personalInformation').style.display = "none";
    document.getElementById('personalInfoForm').reset();
}

let isOrderPending = false;
var newKunde = null;
var stop = false;

/**
 * Creates a new Customer based on the input of the user through the personal information form
 * @param {event} event 
 */
function handleUserData(event) {
    event.preventDefault();
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    newKunde = new Kunde(firstName, lastName, email, phone);

    document.getElementById('personalInformation').style.display = "none";

    if (isOrderPending) {
        continueOrder();
        isOrderPending = false;
    }
}

/**
 * Checks if payment method is set, cancels if not. Opens the personal information window if a year or month ticket is bought.
 * Continues the order if both are not the case.
 */
async function buy_Order() {
    const paymentMethod = document.getElementById('payment-method').value;
    if (paymentMethod === "") {
        document.getElementById('purchaseN').innerHTML = "<h1>Sie haben noch keine Zahlungsmethode ausgewählt!</h1>";
        document.getElementById('purchaseN').style.display = "flex";
        setTimeout(function () {
            document.getElementById('purchaseN').style.display = "none";
            document.getElementById('purchaseN').innerHTML = "<h1>Fehler: Bestellvorgang wurde abgebrochen!</h1>";
        }, 2500);
        return;
    }

    for (var i = 0; i < shoppingCart.length; i++) {
        if (shoppingCart[i]['type'].includes("Ticket") && !shoppingCart[i]['type'].includes('Tag')) {
            document.getElementById('personalInformation').style.display = "block";
            isOrderPending = true;
            return;
        }
    }
    newKunde = null;
    continueOrder();
}

/**
 * Trys to buy the tems from the shoppingcart. Shows order on screen if succesfull, shows error if not
 */
async function continueOrder() {
    var result = await buyOrCheck("buyShoppingCart", { shoppingCart }, newKunde);
    if (result.success[0][0]) {
        document.getElementById('purchaseS').style.display = "flex";
        showOrder();
        document.getElementById('bestellNr').innerHTML = "Ihre Bestellung: " + result.success[0][1];
        document.getElementById('payment-form').reset();
        document.getElementById('personalInfoForm').reset();
    } else {
        document.getElementById('purchaseN').style.display = "flex";
    }
    setTimeout(function () {
        document.getElementById('purchaseS').style.display = "none";
        document.getElementById('purchaseN').style.display = "none";
    }, 3000);
    setTimeout(function () {
        document.getElementById('buyItems').style.display = "none";
        cancel_Order();
    }, 9000);
}

/**
 * Checks if all items form the shoppingcart are in stock
 * @returns A `bool` that shows whether all items in the shoppingcart are available
 */
async function checkIfAvailable() {
    var result = await buyOrCheck("checkAvailableItems", { shoppingCart }, null);
    var boolArray = result.success;
    var everythingIsAvailable = true

    for (var i = 0; i < boolArray.length; i++) {
        var aktItemId = "item_" + i;

        document.getElementById(aktItemId + 'L').style.display = "none";
        document.getElementById(aktItemId + 'nL').style.display = "none";
        if (boolArray[i] == true) {
            document.getElementById(aktItemId + 'L').style.display = "block";
        } else {
            document.getElementById(aktItemId + 'nL').style.display = "block";
            everythingIsAvailable = false;
        }

    }
    return everythingIsAvailable;
}


/**
 * Sends a POST request with the given data to the server and returns the response
 * @param {String} action 
 * @param {*} data 
 * @param {Kunde | null} kunde 
 * @returns the servers response, `null` if the process failed
 */
async function buyOrCheck(action, data, kunde) {
    try {
        const response = await fetch('/shop/buyOrCheck', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ action: action, data: data, kunde: kunde })
        });

        if (response.ok) {
            const result = await response.json();
            return result;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Gets the snacks from the server based on the set filter, generates the html items and shows them on the screen
 * @param {String} filter `"drinks"`, `"sweet"` or `"salty"`
 * @returns the requested data as `json`, `null`if the process failed
 */
async function getSnacks(filter) {
    try {
        var response;
        switch (filter) {
            case "drinks":
                response = await fetch('/terminal/shop/snacks/drinks');
                break;
            case "sweet":
                response = await fetch('/terminal/shop/snacks/sweet');
                break;
            case "salty":
                response = await fetch('/terminal/shop/snacks/salty');
                break;
            default:
                response = await fetch('/terminal/shop/snacks');
                break;
        }

        if (response.ok) {
            const data = await response.json();
            processSnacks(data)
            return data;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Creates HTML Items for the given snacks and displays them on the shop screen
 * @param {*} data the snacks that will be displayed
 */
function processSnacks(data) {
    const specialItems = ["Solary Salad", "Venus Vinegar Chips", "Zodiac Sourcreme Chips", "Galaxie Gummi Bears", "Parsec Peanuts"];
    var products = document.querySelector('.products');
    var tempHTML = '';
    products.style.display = "grid";
    document.querySelector('.tickets').style.display = "none";
    products.innerHTML = '';

    data.forEach(snack => {
        if (!tempHTML.includes(snack.BEZEICHNUNG)) {
            tempHTML += `
                <div class="product_card">
                    <img class="product_image" src="${snack.IMAGE_PATH}" alt="${snack.BEZEICHNUNG} Bild" width="150" height="150">
                    <label class="product_name" for="">${snack.BEZEICHNUNG}</label>
                    <div>
                        <label class="product_price" for="">${snack.VERKAUF_PREIS_STK} €</label>
                      `
            if (!specialItems.includes(snack.BEZEICHNUNG)) {
                tempHTML += `
                            <select class="product_size" name="Size" id="size_${snack.ID}">
                            <optgroup label="Size">
                                <option value="M">M</option>
                                <option value="L">L</option>
                            </optgroup>
                            </select>

                        </div>
                        <button type="button" onclick="add('${snack.ID}', '${snack.BEZEICHNUNG}', '${snack.BESCHREIBUNG}', document.getElementById('size_${snack.ID}').value, '${snack.VERKAUF_PREIS_STK}', 1, '${snack.IMAGE_PATH}')">Add To Cart</button>
                    </div>`;
            }
            else {
                tempHTML += `</div>
                        <button type="button" onclick="add('${snack.ID}', '${snack.BEZEICHNUNG}', '${snack.BESCHREIBUNG}', 'Standard', '${snack.VERKAUF_PREIS_STK}', 1, '${snack.IMAGE_PATH}')">Add To Cart</button>
                    </div>`;
            }

        }
    });

    products.innerHTML = tempHTML;
}

/**
 * Gets the merch from the server based on the set filter, generates the html items and shows them on the screen
 * @param {String} filter `"clothing"`, `"accessoires"`, `"householdItem"`, `"stationery"` or `"salty"`
 * @returns the requested data as `json`, `null`if the process failed
 */
async function getMerch(filter) {
    try {
        var response;
        switch (filter) {
            case "clothing":
                response = await fetch("/terminal/shop/merch/clothing");
                break;
            case "accessoires":
                response = await fetch("/terminal/shop/merch/accessoires");
                break;
            case "householdItem":
                response = await fetch("/terminal/shop/merch/householdItem");
                break;
            case "stationery":
                response = await fetch("/terminal/shop/merch/stationery");
                break;
            case "other":
                response = await fetch("/terminal/shop/merch/other");
                break;
            default:
                response = await fetch("/terminal/shop/merch");
                break;
        }

        if (response.ok) {
            const data = await response.json();
            processMerch(data)
            return data;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Creates HTML Items for the given merch and displays them on the shop screen
 * @param {*} data the snacks that will be displayed
 */
function processMerch(data) {
    const specialItems = [
        "Solar System Socks", "Marsian Mug", "Milkyway Mug", "Uranus USB Stick",
        "Venus Vase", "Jupiter Journal", "Neptune Notebook", "Meteor Magnet",
        "Saturn Sunglasses", "Nebula Napkins", "Uranus Umbrella"
    ];
    var products = document.querySelector('.products');
    var tempHTML = '';
    products.style.display = "grid";
    document.querySelector('.tickets').style.display = "none";

    products.innerHTML = '';

    data.forEach(merch => {
        if (!tempHTML.includes(merch.BEZEICHNUNG)) {
            tempHTML += `
                <div class="product_card">
                    <img class="product_image" src="${merch.IMAGE_PATH}" alt="${merch.BEZEICHNUNG} Bild" width="150" height="150">
                    <label class="product_name" for="">${merch.BEZEICHNUNG}</label>
                    <div>
                        <label class="product_price" for="">${merch.VERKAUF_PREIS_STK} €</label>
                            `
            if (!specialItems.includes(merch.BEZEICHNUNG)) {
                tempHTML += `
                                <select class="product_size" name="Size" id='size_${merch.ID}'>
                                <optgroup label="Size">
                                           <option value="S">S</option>
                                <option value="M">M</option>
                                <option value="L">L</option>
                                </optgroup>
                                </select>
                        </div>
                        <button type="button" onclick="add('${merch.ID}', '${merch.BEZEICHNUNG}', '${merch.BESCHREIBUNG}', document.getElementById('size_${merch.ID}').value, '${merch.VERKAUF_PREIS_STK}', 1, '${merch.IMAGE_PATH}')">Add To Cart</button>
                    </div>`;
            }
            else {
                tempHTML += `</div>
                                <button type="button" onclick="add('${merch.ID}', '${merch.BEZEICHNUNG}', '${merch.BESCHREIBUNG}', 'Standard', '${merch.VERKAUF_PREIS_STK}', 1, '${merch.IMAGE_PATH}')">Add To Cart</button>
                        </div>`;
            }

        }
    });

    products.innerHTML = tempHTML;
}
/**
 * Gets the tickets from the server, generates the html items and shows them on the screen
 * @returns the requested data as `json`, `null`if the process failed
 */
async function getTickets() {
    try {
        var response = await fetch("/terminal/shop/tickets");
        if (response.ok) {
            const data = await response.json();
            processTickets(data)
            return data;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Creates HTML Items for the given tickets and displays them on the shop screen
 * @param {*} data the snacks that will be displayed
 */
function processTickets(data) {

    var products = document.querySelector('.products');
    var tempHTML = '';
    var tickets = document.querySelector('.tickets')
    tickets.style.display = "flex"
    products.style.display = "none";
    products.innerHTML = '';

    data.forEach(ticket => {
        if (!tempHTML.includes(ticket.STUFE)) {
            tempHTML += `
            <div class="ticket_card">
                <div class="pricetag">${ticket.PREIS}€</div>
                <div class="ticket_column">
                    <h1>${ticket.STUFE}</h1>
                    <h2>This ticket allows you to visit all events in the next ${ticket.ZEITRAUM} day(s)</h2>
                    <p>Note that tickets are handed out at the register when showing your receit like other products.
                    </p>
                    <button type="button" style="margin-top: auto" onclick="add(${ticket.ZEITRAUM}, 'Ticket-${ticket.STUFE}', 'Ticket Gültigkeit: ${ticket.ZEITRAUM} Tage','', ${ticket.PREIS}, 1, '${ticket.IMAGE_PATH}')">Add To Cart</button>
                </div>
                <div class="ticket_column" id="${ticket.STUFE}_events">
                    <div>
                        <h2>Events you will have access to:</h2>
                    </div>
                </div>
                <img src="${ticket.IMAGE_PATH}" alt="${ticket.STUFE} Bild">
            </div>
            `
        }
    });
    tickets.innerHTML = tempHTML;
    setEventInfo()
}

var event_day_timer;
var event_month_timer;
var event_year_timer;

/**
 * Sets the Information about events for the tickets. Starts intervals if there are more than 5 events
 */
async function setEventInfo() {
    const display_day = document.getElementById("Tag_events")
    const display_month = document.getElementById("Monat_events")
    const display_year = document.getElementById("Jahr_events")
    const events_day = await getEvents("tag")
    const events_month = await getEvents("monat")
    const events_year = await getEvents("jahr")

    addEvents(events_day.slice(0, 5), display_day)
    if (events_day.length > 5) {
        event_day_timer = eventUpdateTimer(events_day, 8000, display_day)
    }

    addEvents(events_month.slice(0, 5), display_month)
    if (events_month.length > 5) {
        event_month_timer = eventUpdateTimer(events_month, 4000, display_month)
    }

    addEvents(events_year.slice(0, 5), display_year);
    if (events_year.length > 5) {
        event_year_timer = eventUpdateTimer(events_year, 2000, display_year);
    }
}

/**
 * Sets a interval that updates the content of the ticket events in
 * @param {*} data the events that are displayed
 * @param {Number} time the update rate 
 * @param {*} element the html element that contains the events
 * @returns the id of the set interval neccessary for clearing it later
 */
function eventUpdateTimer(data, time, element) {
    currentIndex = 0;
    return setInterval(function () {
        let tempHTML = "";
        tempHTML += '<div><h2> Events you will have access to:</h2 ></div> '
        for (let i = 0; i < 5; i++) {
            currentIndex += 1;
            if (currentIndex >= data.length) {
                currentIndex = 0;
            }
            tempHTML += `<div class="ticket_event"> 
            ${updateTimestamp(data[currentIndex].DATUM)} - ${data[currentIndex].NAME} 
            </div>`
        }
        element.innerHTML = tempHTML;
    }, time);
}

/**
 * Adds all of the eventdata to the given element
 * @param {*} data The event data that will be shown 
 * @param {*} element The HTML Element that the data will be added to
 */
function addEvents(data, element) {
    data.forEach(event => {
        element.innerHTML += `<div class="ticket_event"> 
        ${updateTimestamp(event.DATUM)} - ${event.NAME} 
        </div>`
    })
}

/**
 * Transforms the given timestamp to another format
 * @param {String} timestamp timestamp in DD Mon YYYY HH:MM:ss TMZ format 
 * @returns a Timestamp in DD Mon YYYY HH:MM format
 */
function updateTimestamp(timestamp) {
    // Trenne den String am " - ", um den Datum- und Uhrzeitteil zu extrahieren
    let date_time_part = timestamp.split(' - ')[0];

    // Trenne den Datum- und Uhrzeitteil in seine Bestandteile
    let parts = date_time_part.split(' ');

    // Setze den relevanten Teil (Datum und Zeit ohne Sekunden und Zeitzone) zusammen
    let date = parts.slice(0, 4).join(' '); // Thu, 18 Jul 2024
    let time = parts[4].split(':').slice(0, 2).join(':'); // 15:00

    return `${date} ${time}`;
}

/**
 * Gets the events from the server based on the set filter, generates the html items and shows them on the screen
 * @param {String} filter `"tag"`, `"monat"` or `"jahr"`
 * @returns the requested data as `json`, `null`if the process failed
 */
async function getEvents(filter) {
    try {
        var response;
        switch (filter) {
            case "tag":
                response = await fetch("/terminal/shop/events/day");
                break;
            case "monat":
                response = await fetch("/terminal/shop/events/month");
                break;
            case "jahr":
                response = await fetch("/terminal/shop/events/year");
                break;
            default:
                break;
        }
        if (response.ok) {
            const data = await response.json();
            return data;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Adds article with the given parameters to the shoppincart and displays info text for .75s
 * @param {*} id item id
 * @param {*} type item type
 * @param {*} beschreibung item description
 * @param {*} groesse item size
 * @param {*} preis item price
 * @param {*} anzahl item amount
 * @param {*} image item image
 */
function add(id, type, beschreibung, groesse, preis, anzahl, image) {
    addItemToCart(id, type, beschreibung, groesse, preis, anzahl, image);
    document.getElementById('putItemInCard').style.display = "block";
    setTimeout(function () {
        document.getElementById('putItemInCard').style.display = "none";
    }, 750);
}