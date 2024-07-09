
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

// Event-Listener für DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
    const mediaItem = document.getElementById('mediaGrid');
    if (mediaItem) {
        getMedium(mediaItem);
    }

    const name = document.getElementById('name');
    const description = document.getElementById('description');
    const continue_thema = document.getElementById('continue-thema');
    const save_media = document.getElementById('save-media');

    const nav_thema = document.getElementById('nav-thema');
    const nav_media = document.getElementById('nav-media');
    const nav_date = document.getElementById('nav-date');
    const nav_room = document.getElementById('nav-room');

    // Datum vom Eingabefeld abrufen
    const dateInput = document.getElementById('eventTime');
    const date_btn = document.getElementById('date-btn');

    function checkInputs() {
        // Überprüfe, ob beide Eingabefelder Inhalt haben
        if (name.value.trim() !== '' && description.value.trim() !== '') {
            continue_thema.disabled = false;
            nav_media.classList.remove('disabled');

        } else {
            continue_thema.disabled = true;
            nav_media.classList.add('disabled');
            nav_date.classList.add('disabled');
            nav_room.classList.add('disabled');
        }
    }

    function checkDate() {
        // Überprüfe, ob beide Eingabefelder Inhalt haben
        if (dateInput.value.trim() !== '') {
            date_btn.disabled = false;
            nav_room.classList.remove('disabled');

        } else {
            continue_thema.disabled = true;
            nav_room.classList.add('disabled');
        }
    }

    save_media.addEventListener('click', () => {
        nav_date.classList.remove('disabled');
        filter('nav-date', 'date')
    });

    date_btn.addEventListener('click', () => {
        filter('nav-room', 'room')
        searchForFreeRooms();
    });

    // Event-Listener für Änderungen in den Eingabefeldern hinzufügen
    name.addEventListener('input', checkInputs);
    description.addEventListener('input', checkInputs);
    dateInput.addEventListener('input', checkDate);
});

function loadMedia(elem, medien) {
    // Datenbank lesen
    medien.forEach(medium => {
        var htmlElem =  "<a href='#' class='media-item' onclick='mediaPressed(this)'>"
        htmlElem += `<img src="${medium.IMAGE_PATH}" alt="Media 1" width="150" height="150">`
        if(medium.GALAXIE_NAME) {
            htmlElem += "<h3>" + medium.GALAXIE_NAME + "</h3>"
        }
        if(medium.PLANET_NAME) {
            htmlElem += "<h3>" + medium.PLANET_NAME + "</h3>"
        }
        if(medium.STERN_NAME) {
            htmlElem += "<h3>" + medium.STERN_NAME + "</h3>"
        }
        if(medium.NEBEL_NAME) {
            htmlElem += "<h3>" + medium.NEBEL_NAME + "</h3>"
        }
        if(medium.STERNENBILD_NAME) {
            htmlElem += "<h3>" + medium.STERNENBILD_NAME + "</h3>"
        }
        if(medium.PLANETENSYSTEM_NAME) {
            htmlElem += "<h3>" + medium.PLANETENSYSTEM_NAME + "</h3>"
        }
        if(medium.KOMET_NAME) {
            htmlElem += "<h3>" + medium.KOMET_NAME + "</h3>"
        }

        htmlElem += "<p>" + medium.FORMAT + "</p>"
        htmlElem += "</a>"

        elem.innerHTML += htmlElem;
    });
}

function filter(linkId, sectionId) {
    // event.preventDefault();

    // Alle Navigationslinks deaktivieren
    var navLinks = document.querySelectorAll('.leftComponent a');
    navLinks.forEach(function(link) {
        if (link.id !== linkId){
            link.classList.remove('active');
        }
        else {
            link.classList.add('active');
        }
    });

    // Den geklickten Navigationslink aktivieren
    // event.target.classList.add('active');

    showSection(sectionId);
}

async function getMedium(mediaItem) {
    try {
        var response = await fetch('/intern/events/medien');
        if (response.ok) {
            const data = await response.json();
            loadMedia(mediaItem, data);
            return data;
        }
        else {
            throw new Error('Network response was not ok');
        }
      } catch (error) {
        throw new Error('Fehler beim Laden der Daten:', error);
      }
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
            return data
        } else {
            console.error('Server error:', response.status);
            return null
        }
    } catch (error) {
        console.error('Error:', error);
        return null
    }
}


function processRooms(data, button) {
    var table = document.getElementById("roomTable");

    if(button) {
        var tempHTML = `<tr>
                            <th class="roomName">Bezeichnung</th>
                            <th>Id</th>
                            <th>Kapazität</th>
                            <th>Status</th>
                            <th>Auswahl</th>
                        </tr>`;
    } else {
        var tempHTML = `<tr>
                            <th class="roomName">Bezeichnung</th>
                            <th>Id</th>
                            <th>Kapazität</th>
                            <th>Status</th>
                        </tr>`;
    }

    data.forEach(raum => {
        let status = "frei";
        if (raum.PREIS === null) {
            status = "Abteilungsraum";
        }
        if(button) {
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                    <td><button class"save-btn" onclick="saveEvent()">Wälen</button></td>
                </tr>`;
        } else {
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                </tr>`;
        }
    });
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
            body: JSON.stringify({ bezeichnung: bezeichnung})
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
            body: JSON.stringify({ capacity: Number(capacity)})
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

async function searchForFreeRooms(){
    try {
        // Datum vom Eingabefeld abrufen
        const dateInput = document.getElementById('eventTime').value;

        // Eingabedatum in ein Date-Objekt konvertieren
        const date = new Date(dateInput);

        // Datum in das gewünschte Format für Oracle-Datenbank konvertieren: 'YYYY-MM-DD HH24:MI:SS'
        const formattedDate = ('0' + date.getDate()).slice(-2) + '/' +
            ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
            date.getFullYear();

        // POST-Anfrage mit dem formatierten Datum senden
        var response = await fetch('/intern/rooms/search_free_rooms', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ date: formattedDate }) // Formatiertes Datum hier verwenden
        });
        console.log(response);
        if (response.ok) {
            const result = await response.json();
            console.log(result);
            processRooms(result, true);
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

function toggleMenu(menuId, link) {
    var submenu = document.getElementById(menuId);
    var allLinks = document.querySelectorAll('.menu a');

    allLinks.forEach(function(link) {
        link.classList.remove('selected');
    });

    if (submenu.classList.contains('hidden')) {
        submenu.classList.remove('hidden');
        link.classList.add('selected');
    } else {
        submenu.classList.add('hidden');
        link.classList.remove('selected');
    }
}

async function getPlanets() {
    try {
        response = await fetch("/intern/planets/planetlist");
        if (response.ok) {
            const data = await response.json();
            processPlanets(data)
            return data
        } else {
            console.error('Server error:', response.status);
            return null
        }
    } catch (error) {
        console.error('Error:', error);
        return null
    }
}

function processPlanets(data) {
    var table = document.getElementById("planetTable");
    var tempHTML = `<tr>
                        <th class="roomName">Bezeichnung</th>
                        <th>ID</th>
                        <th>Informationen</th>
                    </tr>`;

    data.forEach(planet => {
        tempHTML += `
                <tr>
                    <td class="roomName">${planet.BEZEICHNUNG}</td>
                    <td>${planet.ID}</td>
                    <td>${planet.INFORMATIONEN}</td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}



function saveEvent() {
    console.log("Not implemented")
}