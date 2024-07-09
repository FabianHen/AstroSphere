// SLEEPTIMER + DISPLAYTIMER = Gesamtzeit bis reset
const IDLETIMER = 50000;
const SLEEPTIMER = 10000;
const STARTCOLOR = { r: 66, g: 4, b: 176 };
const ENDCOLOR = { r: 211, g: 13, b: 164 };

function goBack() {
    window.location.href = window.location.href.split('/', window.location.href.split('/').length - 1).join('/');
}

function collapseFilter(filter) {
    if (filter) {
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
                    case 'ticket_filter':
                        getTicket('all');
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

function sleepTimer() {
    clearTimeout(idle_timeout);
    let rounds_total = SLEEPTIMER / 1000;
    let current_round = rounds_total;
    document.getElementById("sleepTimer").style.display = "flex";
    sleep_timeout = setInterval(function () {
        current_round--;
        const factor = 1 - (current_round / rounds_total);
        const interpolatedColor = interpolateColor(STARTCOLOR, ENDCOLOR, factor);
        console.log(interpolatedColor)
        document.getElementById("timer").style.color = rgbToHex(interpolatedColor.r, interpolatedColor.g, interpolatedColor.b);
        document.getElementById("timer").innerHTML = current_round
        if (current_round < 0) {
            clearInterval(sleep_timeout);
            document.getElementById("sleepTimer").style.display = "none";
            goBack()
        }
    }, 1000);
}

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
}

function interpolateColor(color1, color2, factor) {
    const result = {
        r: Math.round(color1.r + factor * (color2.r - color1.r)),
        g: Math.round(color1.g + factor * (color2.g - color1.g)),
        b: Math.round(color1.b + factor * (color2.b - color1.b))
    };
    return result;
}

window.addEventListener("load", function (e) {
    let params = new URL(document.location).searchParams;
    let selected = params.get("selected");
    if (selected) {
        collapseFilter(selected);
    }
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
    constructor(vorname, nachname, email, telefonnummer){
        this.vorname=vorname;
        this.nachname=nachname;
        this.email=email;
        this.telefonnummer=telefonnummer;
    }
}

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
        if(shoppingCart[i].größe!=""){
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

function deleteItem(id) {
    const aktItem = "item_" + id + "Num";
    document.getElementById(aktItem).value = 0;
    updateShoppingCart(true);
}

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




function goTo_shoppingCart() {
    if (document.getElementById('shoppingCart').style.display == "flex") {
        document.getElementById('shoppingCart').style.display = "none";
    }
    else {
        document.getElementById('shoppingCart').style.display = "flex";
    }
    updateShoppingCart(false);
}

function cancel_Order() {
    shoppingCart = [];
    updateShoppingCart();
    document.getElementById('shoppingCart').style.display = "none";
    document.getElementById('payment-form').reset();
    document.getElementById('personalInfoForm').reset();
}



function cancelUserInput(){
    document.getElementById('personalInformation').style.display = "none";
    document.getElementById('personalInfoForm').reset();
}


let isOrderPending = false;
var newKunde=null;
var stop=false;

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
    newKunde=null;
    continueOrder();
}



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



async function buyOrCheck(action, data, kunde) {
    try {
        const response = await fetch('/shop/buyOrCheck', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ action: action, data: data , kunde: kunde})
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

function processSnacks(data) {
    const specialItems = ["Solary Salad", "Venus Vinegar Chips", "Zodiac Sourcreme Chips", "Galaxie Gummi Bears", "Parsec Peanuts"];
    var products = document.querySelector('.products');
    var tempHTML = '';

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
            else{
                tempHTML += `</div>
                        <button type="button" onclick="add('${snack.ID}', '${snack.BEZEICHNUNG}', '${snack.BESCHREIBUNG}', 'Standard', '${snack.VERKAUF_PREIS_STK}', 1, '${snack.IMAGE_PATH}')">Add To Cart</button>
                    </div>`;
            }

        }
    });

    products.innerHTML = tempHTML;
}


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

function processMerch(data) {
    const specialItems = [
        "Solar System Socks", "Marsian Mug", "Milkyway Mug", "Uranus USB Stick",
        "Venus Vase", "Jupiter Journal", "Neptune Notebook", "Meteor Magnet",
        "Saturn Sunglasses", "Nebula Napkins", "Uranus Umbrella"
    ];
    var products = document.querySelector('.products');
    var tempHTML = '';

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
            else{
                tempHTML += `</div>
                                <button type="button" onclick="add('${merch.ID}', '${merch.BEZEICHNUNG}', '${merch.BESCHREIBUNG}', 'Standard', '${merch.VERKAUF_PREIS_STK}', 1, '${merch.IMAGE_PATH}')">Add To Cart</button>
                        </div>`;
            }

        }
    });

    products.innerHTML = tempHTML;
}

async function getTicket(filter) {
    try {
        var response;
        switch (filter) {
            case "day":
                response = await fetch("/terminal/shop/tickets/day");
                break;
            case "month":
                response = await fetch("/terminal/shop/tickets/month");
                break;
            case "year":
                response = await fetch("/terminal/shop/tickets/year");
                break;
            default:
                response = await fetch("/terminal/shop/tickets");
                break;
        }

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

function processTickets(data) {
    var products = document.querySelector('.products');
    var tempHTML = '';

    products.innerHTML = '';

    data.forEach(ticket => {
        if (!tempHTML.includes(ticket.STUFE)) {
            tempHTML += `
                <div class="product_card">
                    <img class="product_image" src="${ticket.IMAGE_PATH}" alt="${ticket.STUFE} Bild" width="150" height="150">
                    <label class="product_name" for="">${ticket.STUFE}</label>
                    <div>
                        <label class="product_price" for="">${ticket.PREIS} €</label>
                    </div>
                    <button type="button" onclick="add(${ticket.ZEITRAUM}, 'Ticket-${ticket.STUFE}', 'Ticket Gültigkeit: ${ticket.ZEITRAUM} Tage','', ${ticket.PREIS}, 1, '${ticket.IMAGE_PATH}')">Add To Cart</button>
                </div>`;
        }
    });

    products.innerHTML = tempHTML;
}

function add(id, type, beschreibung, groesse, preis, anzahl, image) {
    addItemToCart(id, type, beschreibung, groesse, preis, anzahl, image);
    document.getElementById('putItemInCard').style.display = "block";
    setTimeout(function () {
        document.getElementById('putItemInCard').style.display = "none";
    }, 750);
}