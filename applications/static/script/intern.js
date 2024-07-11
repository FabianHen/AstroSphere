
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

// Funktion, um das aktuelle Datum und die Uhrzeit im richtigen Format zu erhalten
function getCurrentDateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // Monate sind 0-basiert
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}

// Event-Listener für DOMContentLoaded
document.addEventListener('DOMContentLoaded', async function() {
    if ( document.getElementById('nav-events')){
        initEventsPage();
    } else if ( document.getElementById('nav-rooms')){
        await getRooms();
    } else if ( document.getElementById('nav-planets')){
        await getPlanetsystems();
    } else if ( document.getElementById('nav-telescopes')){
        await getTelescopes();
    }
});

async function initEventsPage() {
    const mediaItem = document.getElementById('mediaGrid');
    const save_media = document.getElementById('save-media');
    if (mediaItem) {
        await getMedium(mediaItem);
        let mediaItems = document.querySelectorAll('.media-item');
        mediaItems.forEach(mediaItem => { 
            mediaItem.addEventListener('click', function() {
                if (mediaItem.classList.contains('active')) {
                    nav_date.classList.remove('disabled');
                    save_media.disabled = false;
                }
                else {
                    nav_date.classList.add('disabled');
                    save_media.disabled = true;
                }
            });
        });
    }

    const name = document.getElementById('name');
    const description = document.getElementById('description');
    const continue_thema = document.getElementById('continue-thema');

    const nav_thema = document.getElementById('nav-thema');
    const nav_media = document.getElementById('nav-media');
    const nav_date = document.getElementById('nav-date');
    const nav_room = document.getElementById('nav-room');

    // Datum vom Eingabefeld abrufen
    const dateInput = document.getElementById('eventTime');
    const date_btn = document.getElementById('date-btn');

    dateInput.min = getCurrentDateTime();

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
        filter('nav-date', 'date');
        return;
    });

    date_btn.addEventListener('click', () => {
        filter('nav-room', 'room')
        searchForFreeRooms();
    });

    // Event-Listener für Änderungen in den Eingabefeldern hinzufügen
    name.addEventListener('input', checkInputs);
    description.addEventListener('input', checkInputs);
    dateInput.addEventListener('input', checkDate);

    generateEventTable(true, true);
}

async function getEventDetails(eventId) {
    try {
        var response = await fetch('/intern/events/allEvents');
        var responseMedia = await fetch('/intern/events/medium', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: eventId})
        });
        if (response.ok && responseMedia.ok) {
            const data = await response.json();
            const mediaData = await responseMedia.json();
            data.forEach(event => {
                if (event.ID === eventId) {
                    showEventDetails(event, mediaData);
                }
            });
            // showEventDetails(event);
            return data;
        }
        else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        throw new Error('Fehler beim Laden der Daten:', error);
    }
}

function showEventDetails(event, media) {
    const mainContent = document.getElementById('event-details');

    mainContent.innerHTML = `<h2 style="margin: 30px auto 10px auto;">${event.NAME}</h2>
                            <div class="text-box">
                                ${event.BESCHREIBUNG}
                            </div>
                            <h3 style="margin: 5px auto 0px 30px;">Details:</h3>
                            <p style="margin: 5px auto 0px 60px;">ID: ${event.ID}</p>
                            <p style="margin: 5px auto 0px 60px;">Raum: ${event.RAUM_ID}</p>
                            <p style="margin: 5px auto 0px 60px;">Datum: ${event.DATUM}</p>
                            
                            <h3 style="margin: 5px auto 0px 30px;">Medien:</h3>
                            <div style="display: flex; justify-content: center; margin-top: 30px">
                                <table width="100%" id="media-table">
                                    <tr>
                                        <th>Id</th>
                                        <th>Format</th>
                                        <th>Typ</th>
                                    </tr>
                                </table>
                            </div>`;
    
    var table = document.getElementById('media-table');

    media.forEach(medium => {
        table.innerHTML += `<tr>
                                    <td>${medium.ID}</td>
                                    <td>${medium.FORMAT}</td>
                                    <td>${medium.TYP}</td>
                                </tr>`;
    });
}

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
        htmlElem += "<p sytle='display: none'>" + medium.ID + "</p>"
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

function changeLeftComponent() {
    const nav_create_event = document.getElementById('nav-create-event');
    const nav_events = document.getElementById('nav-events');
    nav_create_event.classList.toggle('disabled');
    nav_events.classList.toggle('disabled');
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
            const freeRooms = await getFreeRooms();
            processRooms(data, freeRooms)
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

async function getFreeRooms() {
    try {
        response = await fetch("/intern/rooms/freeRooms");
        if (response.ok) {
            const data = await response.json();
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

function processEvents(data, all) {
    var eventTable = document.getElementById('event-table');
    var tempHTML = `<tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Datum</th>
                        <th>Raum</th>
                        <th>Action</th>
                    </tr>`;
    data.forEach(event => {
        if (all) {
            tempHTML +=   `<tr>
                                    <td class="roomName" >${event.ID}</td>
                                    <td>${event.NAME}</td>
                                    <td>${event.DATUM}</td>
                                    <td>${event.RAUM_ID}</td>
                                    <td><button class"save-btn" onclick="getEventDetails(${event.ID}), filter('', 'event-details')">Mehr</button></td>
                                </tr>`;
        } else {
            tempHTML += `<tr>
                                    <td>${event.ID}</td>
                                    <td>${event.NAME}</td>
                                    <td>${event.DATUM}</td>
                                    <td>${event.RAUM_ID}</td>
                                    <td><button class"save-btn" onclick="getEventDetails(${event.ID}), filter('', 'event-details')">Bearbeiten</button></td>
                                </tr>`;
        }
    });

    eventTable.innerHTML = tempHTML;
}


function processRooms(data,freeRooms, button) {
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
        let status = "besetzt";
        if (raum.MIET_PREIS == null) {
            status = "Abteilungsraum";
        }
        if(status === "besetzt"){
            freeRooms.forEach(fr => {
                if(raum.ID == fr.ID) status = "frei";
                return;
            });
        }
        if(button) {
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                    <td><button class"save-btn" onclick="saveEvent(${raum.ID})">Wälen</button></td>
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
            const freeRooms = await getFreeRooms();
            processRooms(result, freeRooms);
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
            const freeRooms = await getFreeRooms();
            processRooms(result, freeRooms);
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
        
        if (response.ok) {
            const result = await response.json()
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

async function generateEventTable(fromAll, all){
    try {
        if (fromAll) {
            var response = await fetch('/intern/events/allEvents');
        } else {
            var response = await fetch('/intern/events/mineEvents');
        }
        if (response.ok) {
            var data = await response.json();
            if (!all) {
                data = data.filter(event => {
                    console.log(event)
                    var currentDate = new Date();
                    var eventDate = new Date(event.DATUM);
                    return eventDate >= currentDate;
                })
            }
            processEvents(data, fromAll);
            return data;
        }
        else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        throw new Error('Fehler beim Laden der Daten:', error);
    }
}

async function getPlanetsystems() {
    try {
        response = await fetch("/intern/planets/planetsystemlist");
        if (response.ok) {
            const data = await response.json();
            processPlanetsystems(data)
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

function processPlanetsystems(data) {
    var table = document.getElementById("planetsystemTable");
    var tempHTML = `<tr>
                        <th>ID</th>
                        <th>Bezeichnung</th>
                        <th>Informationen</th>
                        <th>Action</th>
                    </tr>`;

    data.forEach(planetsystem => {
        tempHTML += `
                <tr>
                    <td>${planetsystem.ID}</td>
                    <td>${planetsystem.NAME}</td>
                    <td>${planetsystem.INFORMATIONEN}</td>
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(planetsystem).replace(/"/g, '&quot;')})">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchPlanetensystemByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchPlanetensystemBezeichnungInput').value;
        const response = await fetch('/intern/planets/search_planetsystem_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processPlanetsystems(result);
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
                        <th>ID</th>
                        <th>Bezeichnung</th>
                        <th>Informationen</th>
                        <th>Action</th>
                    </tr>`;

    data.forEach(planet => {
        tempHTML += `
                <tr>
                    <td>${planet.ID}</td>
                    <td>${planet.NAME}</td>
                    <td>${planet.INFORMATIONEN}</td>
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(planet).replace(/"/g, '&quot;')})">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchPlanetByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchPlanetBezeichnungInput').value;
        const response = await fetch('/intern/planets/search_planet_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processPlanets(result);
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

async function getStarimages() {
    try {
        response = await fetch("/intern/planets/starimagelist");
        if (response.ok) {
            const data = await response.json();
            processStarimages(data)
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

function processStarimages(data) {
    var table = document.getElementById("starimageTable");
    var tempHTML = `<tr>
                        <th>ID</th>
                        <th>Bezeichnung</th>
                        <th>Informationen</th>
                        <th>Action</th>
                    </tr>`;

    data.forEach(starimage => {
        tempHTML += `
                <tr>
                    <td>${starimage.ID}</td>
                    <td>${starimage.NAME}</td>
                    <td>${starimage.INFORMATIONEN}</td>
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(starimage).replace(/"/g, '&quot;')})">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchSternenbildByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchSternenbildBezeichnungInput').value;
        const response = await fetch('/intern/planets/search_starimage_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processStarimages(result);
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

async function getStars() {
    try {
        response = await fetch("/intern/planets/starlist");
        if (response.ok) {
            const data = await response.json();
            processStars(data)
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

function processStars(data) {
    var table = document.getElementById("starTable");
    var tempHTML = `<tr>
                        <th>ID</th>
                        <th>Bezeichnung</th>
                        <th>Informationen</th>
                        <th>Action</th>
                    </tr>`;

    data.forEach(star => {
        tempHTML += `
                <tr>
                    <td>${star.ID}</td>
                    <td>${star.NAME}</td>
                    <td>${star.INFORMATIONEN}</td>
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(star).replace(/"/g, '&quot;')})">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchSternByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchSternBezeichnungInput').value;
        const response = await fetch('/intern/planets/search_star_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processStars(result);
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

async function getComets() {
    try {
        response = await fetch("/intern/planets/cometlist");
        if (response.ok) {
            const data = await response.json();
            processComets(data)
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

function processComets(data) {
    var table = document.getElementById("cometTable");
    var tempHTML = `<tr>
                        <th>ID</th>
                        <th>Bezeichnung</th>
                        <th>Informationen</th>
                        <th>Action</th>
                    </tr>`;

    data.forEach(comet => {
        tempHTML += `
                <tr>
                    <td>${comet.ID}</td>
                    <td>${comet.NAME}</td>
                    <td>${comet.INFORMATIONEN}</td>
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(comet).replace(/"/g, '&quot;')})">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

async function searchKometByBezeichnung(){
    try {
        const bezeichnung = document.getElementById('searchKometBezeichnungInput').value;
        const response = await fetch('/intern/planets/search_comet_bezeichnung', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processComets(result);
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

async function saveEvent(roomID) {
    try {
        const name = document.getElementById('name');
        const beschreibung = document.getElementById('description');
        const date = document.getElementById('eventTime');
        const mediaItems = document.querySelectorAll('.media-item active');

        const response = await fetch('/intern/events/book_event', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ datum: date, raum_id: roomID, name: name, beschreibung: beschreibung})
        });
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

var globalDataTelescopes = [];

async function getTelescopes() {
    try {
        response = await fetch("/intern/telescopes/telescopeList");
        if (response.ok) {
            const data = await response.json();
            processTelescopes(data)
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

function processTelescopes(data) {
    var table = document.getElementById("telescopesTable");
    globalDataTelescopes = data;
        var tempHTML = `<tr>
                            <th class="roomName">Name</th>
                            <th>Typ</th>
                            <th>Action</th>
                        </tr>`;

    data.forEach((telescope, index) => {
        
            tempHTML += `
                <tr>
                    <td class="roomName">${telescope.BEZEICHNUNG}</td>
                    <td>${telescope.TYP}</td>
                    <td><button class"save-btn" onclick="showTelescopeDetails(${index}), filter('', 'teslescope-details')">Mehr</button></td>
                </tr>`;
});
    table.innerHTML = tempHTML;
}

async function searchTelescopeByName(){
    try {
        const bezeichnung = document.getElementById('searchTelescopeByNameInput').value;
        const response = await fetch('/intern/telescopes/search_telescope_by_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: bezeichnung})
        });

        if (response.ok) {
            const result = await response.json();
            processTelescopes(result);
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

 function showTelescopeDetails(index) {
    const telescope = globalDataTelescopes[index];
    console.log(telescope);
    const mainContent = document.getElementById('teslescope-details');

    mainContent.innerHTML = `<h2 style="margin: 30px auto 10px auto;">${telescope.BEZEICHNUNG}</h2>
                            <div class="text-box">
                                ${telescope.BESCHREIBUNG}
                            </div>
                            <h3 style="margin: 5px auto 0px 30px;">Details:</h3>
                            <p style="margin: 5px auto 0px 60px;">ID: ${telescope.ID}</p>
                            <p style="margin: 5px auto 0px 60px;">Typ: ${telescope.TYP}</p>
                            <p style="margin: 5px auto 0px 60px;">Tagesmietpreis: ${telescope.TAGES_MIET_PREIS}</p>
                            </div>`;
}

async function openModal(id, object) {
    var modal = document.getElementById(id);
    modal.style.display = "block";
    const form = modal.querySelector("#editForm");
    form.innerHTML = '';

    if(id === "editObject") {
        for (const key in object) {
            if (object.hasOwnProperty(key)) {
                const label = document.createElement('label');
                label.setAttribute('for', key);
                label.textContent = key + ' ';

                const input = document.createElement('input');
                input.setAttribute('type', 'text');
                input.setAttribute('id', key);
                input.setAttribute('name', key);
                input.value = object[key];

                form.appendChild(label);
                form.appendChild(input);
                form.appendChild(document.createElement('br'));
                form.appendChild(document.createElement('br'));
            }
        }

        modal.style.display = "block";
    }
    
    if(id === "addObject") {
        switch (object) {
            case 'Planetensystem':
                try {
                    const data = await getPlanetsystems();
                    if (data && data.length > 0) {
                        generateModal(data, form)
                    } else {
                        console.error('No planet systems found.');
                    }
                } catch (error) {
                    console.error('Error fetching planetsystems:', error);
                }
                break;
            case 'Planet':
                try {
                    const data = await getPlanets();
                    if (data && data.length > 0) {
                        generateModal(data, form)
                    } else {
                        console.error('No planets found.');
                    }
                } catch (error) {
                    console.error('Error fetching planets:', error);
                }
                break;
            case 'Sternenbild':
                try {
                    const data = await getStarimages();
                    if (data && data.length > 0) {
                        generateModal(data, form)
                    } else {
                        console.error('No starimages found.');
                    }
                } catch (error) {
                    console.error('Error fetching starimages:', error);
                }
                break;
            case 'Stern':
                try {
                    const data = await getStars();
                    if (data && data.length > 0) {
                        generateModal(data, form)
                    } else {
                        console.error('No stars found.');
                    }
                } catch (error) {
                    console.error('Error fetching stars:', error);
                }
                break;
            case 'Komet':
                try {
                    const data = await getComets();
                    if (data && data.length > 0) {
                        generateModal(data, form)
                    } else {
                        console.error('No comets found.');
                    }
                } catch (error) {
                    console.error('Error fetching comets:', error);
                }
                break;
            default:
                const label = document.createElement('label');
                label.textContent = 'Default';
                form.appendChild(label);
          }
    }
}

function generateModal(data, form){
    const fetched_object = data[0];
        for (const key in fetched_object) {
            if (fetched_object.hasOwnProperty(key)) {
                const label = document.createElement('label');
                label.setAttribute('for', key);
                label.textContent = key + ' ';

                const input = document.createElement('input');
                input.setAttribute('type', 'text');
                input.setAttribute('id', key);
                input.setAttribute('name', key);

                form.appendChild(label);
                form.appendChild(input);
                form.appendChild(document.createElement('br'));
                form.appendChild(document.createElement('br'));
            }
        }
}

async function closeModal(id) {
    var modal = document.getElementById(id);
    modal.style.display = "none";

}

async function saveChanges(object) {
    try {
        const form = document.getElementById('editForm');
        const formData = new FormData(form);

        let dataObject = {};
        formData.forEach((value, key) => {
            dataObject[key] = value;
        });

        response = responseChanges(object);

        if (response.ok) {
            const result = await response.json();
            processComets(result);
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

async function responseChanges(object){
    let response;
    switch (object) {
        case 'Planetensystem':
            response = await fetch('/intern/planets/save_changes_planetsystem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Planet':
            response = await fetch('/intern/planets/save_changes_planet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Sternenbild':
            response = await fetch('/intern/planets/save_changes_starimage', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Stern':
            response = await fetch('/intern/planets/save_changes_star', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Komet':
            response = await fetch('/intern/planets/save_changes_comet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        default:
            
      }
      return response;
}