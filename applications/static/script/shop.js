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
    constructor(id, type, beschreibung, größe, preis, anzahl, imagePath) {
        this.id=id;
        this.type = type;
        this.beschreibung=beschreibung;
        this.größe=größe;
        this.preis=preis;
        this.anzahl = anzahl;
        this.image = imagePath;
    }
}

function addItemToCart(id, type, beschreibung, größe, preis, anzahl, imagePath) {
    aktItem = new Artikel(id, type, beschreibung, größe, preis, anzahl, imagePath);
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type == aktItem.type) {
            item.anzahl += aktItem.anzahl;
            numberOfItems += aktItem.anzahl;
            createItems();
            return;
        }
    }
    numberOfItems += aktItem.anzahl;
    shoppingCart.push(aktItem);
    createItems();
}

function removeItemFromCart(type, num) {
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type === type) {
            item.anzahl-num;
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
        var newHTMLItem = "<div class='item' id='item_" + i + "'>\n";
        newHTMLItem += "\t<div style='height: 100%; width: 100%;'>\n";
        newHTMLItem += "\t\t<img src='"
        newHTMLItem += shoppingCart[i].image;
        newHTMLItem += "' alt='item image' id='item_" + i + "Img'>\n";
        newHTMLItem += "\t\t<h3 id='item_" + i + "Name'>" + shoppingCart[i].type + "</h3>\n";
        newHTMLItem += "\t\t<div class='line'></div>\n";
        newHTMLItem += "\t\t<p class='beschreibung' id='item_" + i + "Desc'><b>Beschreibung</b><br>"+ shoppingCart[i].beschreibung +"</p>\n";
        newHTMLItem += "\t\t<p class='preis' id='item_" + i + "Preis'>Preis: "+ shoppingCart[i].preis +"</p>\n";
        newHTMLItem += "\t\t<input type='number' min='0' max='10' value='" + shoppingCart[i].anzahl + "'  class='numberOfItems' placeholder='Menge: 1' id='item_" + i + "Num' onchange='updateShoppingCart(true)'>\n";
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
        const itemID="item_"+i;
        const itemNumId = itemID+"Num";

        if(updateNum==true){
            item.anzahl=document.getElementById(itemNumId).value;
            if(item.anzahl<=0){
                removeItemFromCart(item.type, item.anzahl);
            }
        }

        document.getElementById(itemID + 'Num').value = item.anzahl;

        if(!(item.anzahl*item.preis<=0)){
            gesSumme+=item.anzahl*item.preis;
        }
    }
    createItems();
    checkIfAvailable();
    document.getElementById('gesKostenNum').textContent = gesSumme.toFixed(2) + "€";
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
    //shoppingCart = [];
    //updateShoppingCart();
    //document.getElementById('shoppingCart').style.display = "none";
    addItemToCart(8, "Marsian Mug", "Premium-Keramiktasse, 300 ml – Perfekt für Kaffee und Tee. Spülmaschinen- und mikrowellengeeignet.", null, 4.99, 1, "../static/images/products/Marsian_Mug.png");
    addItemToCart(6, "Astro Shirt", "Leichtes Baumwoll-T-Shirt mit klassischem Schnitt und Rundhalsausschnitt. Perfekt für jeden Tag.", "L", 19.99, 2, "../static/images/products/AstroShirt.png");
    addItemToCart(8, "Marsian Mug", "Premium-Keramiktasse, 300 ml – Perfekt für Kaffee und Tee. Spülmaschinen- und mikrowellengeeignet.", null, 4.99, 3, "../static/images/products/Marsian_Mug.png");
    addItemToCart(17, "Venus Vest", "Leichte Steppweste mit isolierender Füllung, ideal für Layering. Mit Reißverschlusstaschen und sportlichem Schnitt.", "M", 15.55, 1, "../static/images/products/Venus_Vest.png");
    updateShoppingCart();
}

async function buy_Order() {
    var result= await buyOrCheck("buyShoppingCart", {shoppingCart});
    if(result.success){
        document.getElementById('purchaseS').style.display="flex";
    }
    else{
        document.getElementById('purchaseN').style.display="flex";
    }
    setTimeout(function(){
        document.getElementById('purchaseS').style.display="none";
        document.getElementById('purchaseN').style.display="none";
    }, 3000);
}


async function checkIfAvailable(){
    var result = await buyOrCheck("checkAvailableItems", {shoppingCart});
    var boolArray = result.success;
    var everythingIsAvailable=true

    for(var i=0;i<boolArray.length;i++){
        var aktItemId="item_"+i;

        document.getElementById(aktItemId+'L').style.display="none";
        document.getElementById(aktItemId+'nL').style.display="none";
        if(boolArray[i]==true){
            document.getElementById(aktItemId+'L').style.display="block";
        }else{
            document.getElementById(aktItemId+'nL').style.display="block";
            everythingIsAvailable=false;
        }
        
    }
    return everythingIsAvailable;
}



async function buyOrCheck(action, data) {
    try {
        const response = await fetch('/shop/buyOrCheck', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ action: action, data: data })
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

