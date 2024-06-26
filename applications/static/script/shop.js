function goBack() {
    window.location.href = window.location.href.split('/', window.location.href.split('/').length - 1).join('/');
}

function collapseFilter(filter) {
    let content = document.getElementById(filter);
    if (content.style.display == "flex") {  
        content.style.display = "none";
    } else {
        content.style.display = "flex";
    }
}



shoppingCart = [];
var numberOfItems = 0;

class Artikel {
    constructor(type, anzahl, preis) {
        this.type = type;
        this.anzahl = anzahl;
        this.preis = preis;
    }
}

function addItemToCart(type, anzahl, preis) {
    aktItem = new Artikel(type, anzahl, preis);
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type === type) {
            item.anzahl += anzahl;
            numberOfItems += anzahl;
            return;
        }
    }
    numberOfItems += anzahl;
    shoppingCart.push(aktItem);
    createItems();
}

function removeItemFromCart(type, anzahl) {
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type === type) {
            item.anzahl -= anzahl;
            if (item.anzahl <= 0) {
                shoppingCart.splice(i, 1);
            }
            return;
        }
    }
    console.log(`Artikel ${type} nicht gefunden.`);
}


function createItems() {
    var newHTMLString = "";
    for (let i = 0; i < shoppingCart.length; i++) {
        var newHTMLItem = "<div class='item' id='item_" + i + 1 + "'>\n";
        newHTMLItem += "\t<div style='height: 100%; width: 100%;'>\n";
        newHTMLItem += "\t\t<img src='../static/images/pictureNotFound.png' alt='item image' id='item_" + i + 1 + "Img'>\n";
        newHTMLItem += "\t\t<h3 id='item_" + i + 1 + "Name'>Item Name</h3>\n";
        newHTMLItem += "\t\t<div class='line'></div>\n";
        newHTMLItem += "\t\t<p class='beschreibung' id='item_" + i + 1 + "Desc'><b>Beschreibung</b><br>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, </p>\n";
        newHTMLItem += "\t\t<p class='preis' id='item_" + i + 1 + "Preis'>Preis: 00.00€</p>\n";
        newHTMLItem += "\t\t<input type='number' min='0' max='7' class='numberOfItems' placeholder='Menge: 1' id='item_" + i + 1 + "Num'>\n";
        newHTMLItem += "\t\t<p class='Lager' id='item_" + i + 1 + "L'>Auf Lager</p>\n";
        newHTMLItem += "\t\t<p class='nLager' id='item_" + i + 1 + "nL'>Nicht Auf Lager</p>\n";
        newHTMLItem += "\t</div>\n</div>";

        newHTMLString += newHTMLItem + "\n\n";

    }

    document.getElementById('itemList').innerHTML = newHTMLString;
}


function updateShoppingCart() {
    var gesSumme = 0.0;
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];

        var aktType = item.type;
        var aktPreis = item.preis;
        var aktAnzahl = item.anzahl;
        console.log("aktItem: " + aktType + " " + aktPreis + " " + aktAnzahl);

        document.getElementById('item_' + i + 1 + 'Name').innerHTML = aktType;
        document.getElementById('item_' + i + 1 + 'Preis').innerHTML = "Preis: " + aktPreis + "€";
        document.getElementById('item_' + i + 1 + 'Num').value = aktAnzahl;

        gesSumme += item.anzahl * item.preis;
    }

    document.getElementById('gesKostenNum').textContent = gesSumme + "€";
}








function goTo_shoppingCart() {
    if (document.getElementById('shoppingCart').style.display == "flex") {
        document.getElementById('shoppingCart').style.display = "none";
    }
    else {
        document.getElementById('shoppingCart').style.display = "flex";
    }

}

function cancel_Order() {
    console.log("cancel Order");
    shoppingCart = [];
    document.getElementById('shoppingCart').style.display = "none";
}

function buy_Order() {
    console.log("buy Order");

    //send current shopping cart to python program (there it should be connected with the database)

    addItemToCart("Tasse", 5, 4.99);
    addItemToCart("T-Shirt", 5, 19.99);
    addItemToCart("Tasse", 2, 4.99);
    updateShoppingCart();
}

