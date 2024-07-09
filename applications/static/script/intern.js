
function showSection(sectionId) {
    // Alle Inhaltsbereiche ausblenden
    var sections = document.querySelectorAll('.mainContent');
    sections.forEach(function(section) {
        section.classList.remove('active');
    });

    // Den ausgewählten Inhaltsbereich anzeigen
    var selectedSection = document.getElementById(sectionId);
    selectedSection.classList.add('active');
}


function filter(event, sectionId) {
    event.preventDefault();

    // Alle Navigationslinks deaktivieren
    var navLinks = document.querySelectorAll('.leftComponent a');
    navLinks.forEach(function(link) {
        link.classList.remove('active');
    });

    // Den geklickten Navigationslink aktivieren
    event.target.classList.add('active');

    showSection(sectionId);
}

function mediaPressed(elem){
    elem.classList.toggle('active');
}

function goToEvents() {
    window.location.href = '/intern/events';
}

async function goToRooms() {
    window.location.href = '/intern/rooms';
}

function goToPlanets() {
    window.location.href = '/intern/planets';
}

function goToTelescopes() {
    window.location.href = '/intern/telescopes';
}

function goBackHome() {
    window.location.href = '/';
}

async function getRooms() {
    try {
        response = await fetch("/intern/rooms/roomlist");
        if (response.ok) {
            const data = await response.json();
            processRooms(data)
        } else {
            console.error('Server error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}


function processRooms(data) {
    var table = document.getElementById("roomTable");
    var tempHTML = "";

    var rowCount = table.rows.length;
    for (var i = rowCount - 1; i > 0; i--) {
        table.deleteRow(i);
    }
    console.log("delete rows");
    data.forEach(raum => {
        let status = "frei";
        if (raum.PREIS === null) {
            status = "Abteilungsraum";
        }
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchRaumByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchRaumBezeichnungInput').value;
        const response = await fetch('/intern/rooms/search_room_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: number})
        });

        if (response.ok) {
            const result = await response.json();
            processRooms(result);
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

async function searchRaumByCapacity(){
    try {
        const capacity = document.getElementById('searchRaumCapacityInput').value;
        const response = await fetch('/intern/rooms/search_room_capacity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ capacity: number})
        });

        if (response.ok) {
            const result = await response.json();
            processRooms(result);
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