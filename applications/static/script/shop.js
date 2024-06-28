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
    constructor(type, anzahl, preis, imagePath) {
        this.type = type;
        this.anzahl = anzahl;
        this.preis = preis;
        this.image = imagePath;
    }
}

function addItemToCart(type, anzahl, preis, imagePath) {
    aktItem = new Artikel(type, anzahl, preis, imagePath);
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

function removeItemFromCart(type) {
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        if (item.type === type) {
            if (item.anzahl <= 0) {
                shoppingCart.splice(i, 1);
                createItems();
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
        newHTMLItem += "\t\t<p class='beschreibung' id='item_" + i + "Desc'><b>Beschreibung</b><br>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, </p>\n";
        newHTMLItem += "\t\t<p class='preis' id='item_" + i + "Preis'>Preis: "+ shoppingCart[i].preis +"</p>\n";
        newHTMLItem += "\t\t<input type='number' min='0' max='7' value='" + shoppingCart[i].anzahl + "'  class='numberOfItems' placeholder='Menge: 1' id='item_" + i + "Num' onchange='updateShoppingCart(true, this.value)'>\n";
        newHTMLItem += "\t\t<p class='Lager' id='item_" + i + "L' style='display: block;'>Auf Lager</p>\n";
        newHTMLItem += "\t\t<p class='nLager' id='item_" + i + "nL' style='display: none;'>Nicht Auf Lager</p>\n";
        newHTMLItem += "\t</div>\n</div>";

        newHTMLString += newHTMLItem + "\n\n";

    }

    document.getElementById('itemList').innerHTML = newHTMLString;
    checkIfShoppingCartIsAvailable(false);
}



function updateShoppingCart(updateNum, value) {
    var gesSumme = 0.0;
    for (let i = 0; i < shoppingCart.length; i++) {
        const item = shoppingCart[i];
        const itemID="item_"+i;
        const itemNumId = itemID+"Num";

        if(updateNum==true){
            item.anzahl=document.getElementById(itemNumId).value;
            console.log(item.type+" "+item.anzahl);
            if(item.anzahl<=0){
                removeItemFromCart(item.type, item.anzahl);
            }
        }
        var aktAnzahl = item.anzahl;

        document.getElementById(itemID + 'Num').value = aktAnzahl;


        gesSumme += item.anzahl * item.preis;
    }
    createItems();
    checkIfShoppingCartIsAvailable();
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
    shoppingCart = [];
    document.getElementById('shoppingCart').style.display = "none";
}

async function buy_Order() {
    addItemToCart("Marsian Mug", 5, 4.99, "../static/images/products/Marsian_Mug.png");
    addItemToCart("Astro Shirt", 5, 19.99, "../static/images/products/AstroShirt.png");
    addItemToCart("Marsian Mug", 2, 4.99, "../static/images/products/Marsian_Mug.png");
    addItemToCart("Venus Vest", 5, 4.99, "../static/images/products/Venus_Vest.png");
    updateShoppingCart();
    checkIfShoppingCartIsAvailable(true);


}

async function checkIfShoppingCartIsAvailable(purchaseOrder){
    try{
        var result= await sendData("checkAvailableItems", {shoppingCart});
        if(checkIfAvailable(result) && purchaseOrder){
            var result= await sendData("buyShoppingCart", {shoppingCart});
            if(result.success){
                document.getElementById('purchaseS').style.display="flex";
            }
            else{
                document.getElementById('purchaseN').style.display="flex";
            }
            setTimeout(() => {
                document.getElementById('purchaseS').style.display = "none";
                document.getElementById('purchaseN').style.display = "none";
            }, 3000);
        }
        else{

        }
    } catch(error){
        console.log("Error during checkAvailable processing: ", error);
    }
}

async function checkIfAvailable(result){
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



async function sendData(action, data) {
    try {
        const response = await fetch('/send_data', {
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

