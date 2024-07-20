// Array of all active Media
let activeMedia = [];

/**
 * Event listener for DOMContentLoaded.
 * Initializes specific sections based on the presence of certain elements.
 */
document.addEventListener('DOMContentLoaded', async function() {
    if (document.getElementById('nav-events')) {
        initEventsPage();
    } else if (document.getElementById('nav-rooms')) {
        await getRooms();
    } else if (document.getElementById('nav-planets')) {
        await getPlanetsystems();
    } else if (document.getElementById('nav-telescopes')) {
        await getTelescopes();
    }
});

// =============================================================================================================================
// SECTION: Events
// =============================================================================================================================

/**
 * Gets the current date and time formatted as 'YYYY-MM-DDTHH:MM'.
 *
 * @returns {string} The formatted date and time.
 */
function getCurrentDateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are 0-based
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}

/**
 * Initializes the events page by setting up event listeners and loading necessary data.
 */
async function initEventsPage() {
    const mediaItem = document.getElementById('mediaGrid');
    const save_media = document.getElementById('save-media');
    if (mediaItem) {
        await getMedium(mediaItem);
        let mediaItems = document.querySelectorAll('.media-item');
        mediaItems.forEach(mediaItem => { 
            mediaItem.addEventListener('click', function() {
                if (activeMedia.length > 0) {
                    nav_date.classList.remove('disabled');
                    save_media.disabled = false;
                    return;
                } else {
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

    // Set the minimum date for the date input
    const dateInput = document.getElementById('eventTime');
    const date_btn = document.getElementById('date-btn');

    dateInput.min = getCurrentDateTime();

    function checkDate() {
        // Check if the date input has a value
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
        filter('nav-room', 'room');
        searchForFreeRooms();
    });

    // Add event listeners for input changes
    name.addEventListener('input', checkInputs);
    description.addEventListener('input', checkInputs);
    dateInput.addEventListener('input', checkDate);

    generateEventTable(true, true);
}

/**
 * Checks the inputs of the name and description fields and enables or disables the continue button accordingly.
 */
function checkInputs() {
    const name = document.getElementById('name');
    const description = document.getElementById('description');
    const continue_thema = document.getElementById('continue-thema');
    const nav_thema = document.getElementById('nav-thema');
    const nav_media = document.getElementById('nav-media');
    const nav_date = document.getElementById('nav-date');
    const nav_room = document.getElementById('nav-room');

    // Check if both name and description inputs have values
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

/**
 * Fetches event details and related media from the server and displays them.
 *
 * @param {number} eventId - The ID of the event to fetch details for.
 * @returns {Promise<Object[]>} The event details.
 * @throws Will throw an error if the network response is not ok.
 */
async function getEventDetails(eventId) {
    try {
        var response = await fetch('/intern/events/allEvents');
        var responseMedia = await fetch('/intern/events/medium', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: eventId })
        });
        if (response.ok && responseMedia.ok) {
            const data = await response.json();
            const mediaData = await responseMedia.json();
            data.forEach(event => {
                if (event.ID === eventId) {
                    showEventDetails(event, mediaData);
                }
            });
            return data;
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        throw new Error('Error loading data: ' + error);
    }
}

/**
 * Displays the details of a specific event along with its media.
 *
 * @param {Object} event - The event object containing event details.
 * @param {Object[]} media - An array of media objects related to the event.
 */
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

/**
 * Loads media items into a specified HTML element.
 *
 * @param {HTMLElement} elem - The HTML element to load media items into.
 * @param {Object[]} medien - An array of media objects to load.
 */
function loadMedia(elem, medien) {
    // Load media items into the specified element
    medien.forEach(medium => {
        var htmlElem = `<a href='#' class='media-item' onclick='mediaPressed(this, ${medium.ID})'>`;
        htmlElem += `<img src="${medium.IMAGE_PATH}" alt="Media 1" width="150" height="150">`;
        if (medium.GALAXIE_NAME) {
            htmlElem += "<h3>" + medium.GALAXIE_NAME + "</h3>";
        }
        if (medium.PLANET_NAME) {
            htmlElem += "<h3>" + medium.PLANET_NAME + "</h3>";
        }
        if (medium.STERN_NAME) {
            htmlElem += "<h3>" + medium.STERN_NAME + "</h3>";
        }
        if (medium.NEBEL_NAME) {
            htmlElem += "<h3>" + medium.NEBEL_NAME + "</h3>";
        }
        if (medium.STERNENBILD_NAME) {
            htmlElem += "<h3>" + medium.STERNENBILD_NAME + "</h3>";
        }
        if (medium.PLANETENSYSTEM_NAME) {
            htmlElem += "<h3>" + medium.PLANETENSYSTEM_NAME + "</h3>";
        }
        if (medium.KOMET_NAME) {
            htmlElem += "<h3>" + medium.KOMET_NAME + "</h3>";
        }

        htmlElem += "<p>" + medium.FORMAT + "</p>";
        htmlElem += "<p style='display: none'>" + medium.ID + "</p>";
        htmlElem += "</a>";

        elem.innerHTML += htmlElem;
    });
}

/**
 * Fetches the media items from the server and loads them into the specified element.
 *
 * @param {HTMLElement} mediaItem - The HTML element to load media items into.
 * @returns {Promise<Object[]>} The media data.
 * @throws Will throw an error if the network response is not ok.
 */
async function getMedium(mediaItem) {
    try {
        var response = await fetch('/intern/events/medien');
        if (response.ok) {
            const data = await response.json();
            loadMedia(mediaItem, data);
            return data;
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        throw new Error('Error loading data: ' + error);
    }
}

/**
 * Toggles the 'active' class on a media element and adds/removes its ID from the active media array.
 *
 * @param {HTMLElement} elem - The HTML element representing the media item.
 * @param {number} id - The ID of the media item.
 */
function mediaPressed(elem, id) {
    elem.classList.toggle('active');
    const index = activeMedia.indexOf(id);
    if (index === -1) {
        // Element is not present, add it
        activeMedia.push(id);
    } else {
        // Element is present, remove it
        activeMedia.splice(index, 1);
    }
}

/**
 * Processes the events data and populates the event table with the information.
 *
 * @param {Object[]} data - The array of event objects.
 * @param {boolean} all - Whether to display all events or only specific ones.
 */
function processEvents(data, all) {
    var eventTable = document.getElementById('event-table');
    var tempHTML = `<tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Date</th>
                        <th>Room</th>
                        <th>Action</th>
                    </tr>`;
    data.forEach(event => {
        if (all) {
            tempHTML += `<tr>
                            <td class="roomName">${event.ID}</td>
                            <td>${event.NAME}</td>
                            <td>${event.DATUM}</td>
                            <td>${event.RAUM_ID}</td>
                            <td><button class="save-btn" onclick="getEventDetails(${event.ID}), filter('', 'event-details')">More</button></td>
                        </tr>`;
        } else {
            tempHTML += `<tr>
                            <td>${event.ID}</td>
                            <td>${event.NAME}</td>
                            <td>${event.DATUM}</td>
                            <td>${event.RAUM_ID}</td>
                            <td><button class="save-btn" onclick="getEventDetails(${event.ID}), filter('', 'event-details')">Edit</button></td>
                        </tr>`;
        }
    });

    eventTable.innerHTML = tempHTML;
}


/**
 * Generates the event table by fetching data from the server.
 *
 * @param {boolean} fromAll - Indicates whether to fetch all events or only the user's events.
 * @param {boolean} all - Indicates whether to include past events.
 * @returns {Promise<Object[]>} The event data.
 * @throws Will throw an error if the network response is not ok.
 */
async function generateEventTable(fromAll, all) {
    try {
        var response = fromAll ? await fetch('/intern/events/allEvents') : await fetch('/intern/events/mineEvents');
        
        if (response.ok) {
            var data = await response.json();
            
            if (!all) {
                data = data.filter(event => {
                    var currentDate = new Date();
                    var eventDate = new Date(event.DATUM);
                    return eventDate >= currentDate;
                });
            }
            
            processEvents(data, fromAll);
            return data;
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        throw new Error('Error loading data: ' + error);
    }
}

/**
 * Saves the event by sending a request to the server with event and room details.
 *
 * @param {number} roomID - The ID of the room to book.
 * @returns {Promise<void>} 
 */
async function saveEvent(roomID) {
    try {
        const name = document.getElementById('name');
        const beschreibung = document.getElementById('description');
        const date = document.getElementById('eventTime');

        // Convert the input date to a Date object
        const elem_date = new Date(date.value);

        // Convert date to the desired format for Oracle database: 'YYYY-MM-DD HH24:MI:SS'
        const formattedDate_event = ('0' + elem_date.getDate()).slice(-2) + '/' +
            ('0' + (elem_date.getMonth() + 1)).slice(-2) + '/' +
            elem_date.getFullYear() + ' ' +
            ('0' + elem_date.getHours()).slice(-2) + ':' + ('0' + elem_date.getMinutes()).slice(-2) + ':' + ('0' + elem_date.getSeconds()).slice(-2);

        const formattedDate_room = ('0' + elem_date.getDate()).slice(-2) + '/' +
            ('0' + (elem_date.getMonth() + 1)).slice(-2) + '/' +
            elem_date.getFullYear();

        const response = await fetch('/intern/events/book_event', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ datum: formattedDate_event, raum_id: roomID, name: name.value, beschreibung: beschreibung.value })
        });

        if (response.ok) {
            const result = await response.json();
            console.log('Event booked successfully:', result);

            const response_room = await fetch('/intern/rooms/book_room', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ raum_id: roomID, date: formattedDate_room })
            });

            if (response_room.ok) {
                for (const medium_id of activeMedia) {
                    await fetch('/intern/events/book_medium', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ medium_id: parseInt(medium_id) })
                    });
                }

                resetEvents();
            }
        } else {
            console.error('Server error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * Resets the event creation form and input fields.
 */
function resetEvents() {
    document.getElementById('name').value = '';
    document.getElementById('description').value = '';
    document.getElementById('eventTime').value = '';
    
    let mediaItems = document.querySelectorAll('.media-item');
    mediaItems.forEach(mediaItem => { 
        mediaItem.classList.remove('active');
    });
    
    checkInputs();
}


// =============================================================================================================================
// SECTION: Rooms
// =============================================================================================================================

// array to help all functions to access current rooms without needing to await a Promise
var globalDataRooms = [];

/**
 * Fetches all rooms and processes them into HTML-elements
 * 
 * @returns {Promise<Object[]>}
 */
async function getRooms() {
    try {
        response = await fetch("/intern/rooms/roomlist");
        if (response.ok) {
            const data = await response.json();
            const freeRooms = await getFreeRooms();
            globalDataRooms = data;
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

/**
 * fetches all currently free rooms
 * 
 * @returns {Promise<Object[]>}
 */
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

/**
 * trandforms Date into a string-format accepted by HTML date-input component
 * 
 * @param {Date} dateObject 
 * @returns {string}
 */
function toDateInputValue(dateObject){
    const local = new Date(dateObject);
    local.setMinutes(dateObject.getMinutes() - dateObject.getTimezoneOffset());
    return local.toJSON().slice(0,10);
};

/**
 * transforms room-database-objects into HTML components
 * 
 * @param {Object[]} data - rooms to show
 * @param {Object[]} freeRooms - rooms that are currently free
 * @param {boolean} button - indicator to show slightly different content
 */
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
                            <th>Aktion</th>
                        </tr>`;
    }

    data.forEach((raum, index) => {
        let status = "besetzt";
        if (raum.ABTEILUNG_ID !== null && raum.ABTEILUNG_ID !== 5 && raum.ABTEILUNG_ID !== 7) {
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
                    <td><button class"save-btn" onclick="saveEvent(${raum.ID}), filter('nav-all', 'events-container'), changeLeftComponent()">Wälen</button></td>
                </tr>`;
        } else {
            if(status !== "Abteilungsraum"){
                const today = new Date();
                const defaultValue = toDateInputValue(today);
                tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                    <td><input type="date" id="bookRoomInput" value="${defaultValue}" min="${defaultValue}"><button class"save-btn"  onclick="bookRoom(${index})">buchen</button></td>
                </tr>`;
            } else {
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITAT}</td>
                    <td class="${status}">${status}</td>
                    <td></td>
                </tr>`;
            }
        }
    });
    table.innerHTML = tempHTML;
}

/**
 * tries to book a specific room
 * 
 * checks if room is available on wished date and then books it with
 * writing into the databank
 * 
 * if the room is not available push an alert as response for the user
 * 
 * @param {number} index - index of room to book
 * @returns {Promise<Object[]>}
 */
async function bookRoom(index){
    try {
        const room = globalDataRooms[index];
        const dateInput = document.getElementById('bookRoomInput').value;
         const date = new Date(dateInput);

        // Convert date to the desired format for Oracle database: 'DD/MM/YYYY'
        const formattedDate = ('0' + date.getDate()).slice(-2) + '/' +
            ('0' + (date.getMonth() + 1)).slice(-2) + '/' +
            date.getFullYear();
            
        const canBook = await searchForFreeRooms(true, index);
        if( canBook){
        const response = await fetch('/intern/rooms/book_room', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ raum_id: room.ID, date: formattedDate})
        });
        if (response.ok) {
            const result = await response.json();
            getRooms();
            return result;
        } else {
            console.error('Server error:', response.status);
            return null;
        }
    } else {
        alert("Raum ist zu dieser Zeit bereits gebucht.")
    }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Filters rooms by name input
 * 
 * @returns {Promise<Object[]>}
 */
async function searchRoomByName(){
    try {
        const name = document.getElementById('searchRoomByNameInput').value;
        const response = await fetch('/intern/rooms/search_room_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ bezeichnung: name})
        });

        if (response.ok) {
            const result = await response.json();
            const freeRooms = await getFreeRooms();
            globalDataRooms = result;
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

/**
 * filters rooms by capacity input
 * 
 * @returns {Promise<Object[]>}
 */
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
            globalDataRooms = result;
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

/**
 * searches for rooms that are available on a specific date
 * 
 * to prevent code duplication this function returns either a list of free rooms 
 * for a specified date or a boolean which indicates whether a specific room
 * is free during that day
 * 
 * second is true if it is called by bookRoom
 * 
 * @param {boolean} booking - indicator that bookRoom calls this 
 * @param {number} index - index of wished room
 * @returns {Promise<Object[]>}
 */
async function searchForFreeRooms(booking,index){
    try {
        let dateInput;
        let room;
        if(booking){
             dateInput = document.getElementById('bookRoomInput').value;
            room = globalDataRooms[index];
        }else {
            // Datum vom Eingabefeld abrufen
             dateInput = document.getElementById('eventTime').value;
        }

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
            const freeRooms = await getFreeRooms();
            if(booking){
                let roomIsFree = false; 
                result.forEach((r) => {
                    if(room.ID === r.ID) roomIsFree = true;
                });
                return roomIsFree;
            } else {
                const toProcess = result.filter((r)=> r.ABTEILUNG_ID == 5);
                processRooms(toProcess, freeRooms, true);
            }
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

// ===============================================================================================================================
// SECTION: Planets
// ===============================================================================================================================

/**
 * Toggles the menu used for the sidebar of the planetdata section
 */
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

/**
 * Gets every object of the planetsystemlist and gives it to the processing method
 */
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

/**
 * Processes the given data to generate a table for the specified attributes of every object
 * @param {*} data contains the objects from which the value of every attriute is taken
 */
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
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(planetsystem).replace(/"/g, '&quot;')},'Planetensystem')">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

/**
 * Searches planetsystems by the entered value of 'Bezeichnung' and updates the objectlist
 */
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

/**
 * Gets every object of the planetlist and gives it to the processing method
 */
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

/**
 * Processes the given data to generate a table for the specified attributes of every object
 * @param {*} data contains the objects from which the value of every attriute is taken
 */
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
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(planet).replace(/"/g, '&quot;')},'Planet')">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

/**
 * Searches planets by the entered value of 'Bezeichnung' and updates the objectlist
 */
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

/**
 * Gets every object of the starimagelist and gives it to the processing method
 */
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

/**
 * Processes the given data to generate a table for the specified attributes of every object
 * @param {*} data contains the objects from which the value of every attriute is taken
 */
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
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(starimage).replace(/"/g, '&quot;')},'Sternenbild')">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

/**
 * Searches starimages by the entered value of 'Bezeichnung' and updates the objectlist
 */
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

/**
 * Gets every object of the starlist and gives it to the processing method
 */
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

/**
 * Processes the given data to generate a table for the specified attributes of every object
 * @param {*} data contains the objects from which the value of every attriute is taken
 */
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
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(star).replace(/"/g, '&quot;')},'Stern')">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

/**
 * Searches stars by the entered value of 'Bezeichnung' and updates the objectlist
 */
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

/**
 * Gets every object of the cometlist and gives it to the processing method
 */
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

/**
 * Processes the given data to generate a table for the specified attributes of every object
 * @param {*} data contains the objects from which the value of every attriute is taken
 */
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
                    <td><button class"save-btn" onclick="openModal('editObject', ${JSON.stringify(comet).replace(/"/g, '&quot;')},'Komet')">Edit</button></td>
                </tr>`;
        }
    );
    table.innerHTML = tempHTML;
}

/**
 * Searches comets by the entered value of 'Bezeichnung' and updates the objectlist
 */
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

/**
 * Opens a modal to either add or edit an object of the opened category
 * @param {*} id is the id of the not shown modal
 * @param {*} object is the given object for generating the content of the modal
 * @param {*} type defines which category the modal was opened in
 */
async function openModal(id, object, type) {
    var modal = document.getElementById(id);
    modal.style.display = "block";
    
    if(id === "addObject") {
        const form = document.getElementById('editForm1');
        form.innerHTML = '';
        switch (object) {
            case 'Planetensystem':
                try {
                    const data = await getPlanetsystems();
                    if (data && data.length > 0) {
                        generateModal(data, form, type)
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
                        generateModal(data, form, type)
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
                        generateModal(data, form, type)
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
                        generateModal(data, form, type)
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
                        generateModal(data, form, type)
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

    if(id === "editObject") {
        const form = document.getElementById('editForm2');
        form.innerHTML = '';
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
                    if (key === 'ID') {
                        input.setAttribute('readonly', 'true');
                    }

                    form.appendChild(label);
                    form.appendChild(input);
                    form.appendChild(document.createElement('br'));
                    form.appendChild(document.createElement('br'));
                
            }
        }
        const button = document.createElement('button');
        button.setAttribute('type', 'button');
        button.setAttribute('class', 'button round');
        button.setAttribute('onclick', `saveChanges('${type}'), closeModal('editObject')`);
        button.textContent = 'Speichern';
        form.appendChild(button);

        modal.style.display = "block";
    }
}

/**
 * Generates the content of a modal  
 * @param {*} data are the objects of the category
 * @param {*} form is the form of either the add or the edit modal
 * @param {*} type defines which category the modal was opened in
 */
function generateModal(data, form, type){
    //Take the first object as a template
    const fetched_object = data[0];
    for (const key in fetched_object) {
        if (fetched_object.hasOwnProperty(key)) {
            if(key != 'ID'){
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
    const button = document.createElement('button');
    button.setAttribute('type', 'button');
    button.setAttribute('class', 'button round');
    button.setAttribute('onclick', `addChanges('${type}'), closeModal('addObject')`);
    button.textContent = 'Speichern';
    form.appendChild(button);
}

/**
 * Closes a opened modal
 * @param {*} id is the id of the modal that has to be closed
 */
async function closeModal(id) {
    var modal = document.getElementById(id);
    modal.style.display = "none";

}

/**
 * Adds the changes from the add modal
 * @param {*} object is the category the changes are added to
 */
async function addChanges(object) {
    try {
        const form = document.getElementById('editForm1');
        const formData = new FormData(form);

        let dataObject = {};
        formData.forEach((value, key) => {
            dataObject[key] = value;
        });
        response = responseAddedChanges(object, dataObject);

    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Saves the changes from the edit modal
 * @param {*} object is the category the changes are saved into
 */
async function saveChanges(object) {
    try {
        const form = document.getElementById('editForm2');
        const formData = new FormData(form);

        let dataObject = {};
        formData.forEach((value, key) => {
            dataObject[key] = value;
        });
        response = responseSavedChanges(object, dataObject);

    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

/**
 * Responses to the added changes and adds them to the specified category
 * @param {*} object is the category the changes are added to
 * @param {*} dataObject is the object with the added changes
 */
async function responseAddedChanges(object, dataObject){
    let response;
    switch (object) {
        case 'Planetensystem':
            response = await fetch('/intern/planets/add_changes_planetsystem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Planet':
            response = await fetch('/intern/planets/add_changes_planet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Sternenbild':
            response = await fetch('/intern/planets/add_changes_starimage', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Stern':
            response = await fetch('/intern/planets/add_changes_star', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataObject)
            });
            break;
        case 'Komet':
            response = await fetch('/intern/planets/add_changes_comet', {
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

/**
 * Responses to the saved changes and saves them into the specified category
 * @param {*} object is the category the changes are saved into
 * @param {*} dataObject is the object with the saved changes
 */
async function responseSavedChanges(object, dataObject){
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

// =============================================================================================================================
// SECTION: Telescopes
// =============================================================================================================================

// current telescope objects
var globalDataTelescopes = [];

/**
 * fetch all telescope data from databank
 * 
 * @returns {Promise<Object[]>}
 */
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

/**
 * tranform database date into HTML components
 * 
 * @param {Object[]} data 
 */
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

/**
 * filter telescopes by names per stored procedure
 * 
 * @returns {Promise<Object[]>}
 */
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

/**
 * shows detailed view of specific telescope
 * 
 * @param {number} index - current telescope
 */
 function showTelescopeDetails(index) {
    const telescope = globalDataTelescopes[index];
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

// =============================================================================================================================
// SECTION: Navigation
// =============================================================================================================================

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

/**
 * Shows a specific section of the page by its ID.
 * Hides all other sections.
 *
 * @param {string} sectionId - The ID of the section to show.
 */
function showSection(sectionId) {
    // Hide all content sections
    var sections = document.querySelectorAll('.mainContent');
    sections.forEach(function(section) {
        section.classList.remove('active');
    });

    // Show the selected content section
    var selectedSection = document.getElementById(sectionId);
    selectedSection.classList.add('active');
}

/**
 * Filters the navigation links and shows the selected section.
 *
 * @param {string} linkId - The ID of the navigation link to activate.
 * @param {string} sectionId - The ID of the section to display.
 */
function filter(linkId, sectionId) {
    // Deactivate all navigation links
    var navLinks = document.querySelectorAll('.leftComponent a');
    navLinks.forEach(function(link) {
        if (link.id !== linkId) {
            link.classList.remove('active');
        } else {
            link.classList.add('active');
        }
    });

    showSection(sectionId);
}

/**
 * Toggles the visibility of the 'create event' and 'events' navigation links.
 * Resets the events.
 */
function changeLeftComponent() {
    const nav_create_event = document.getElementById('nav-create-event');
    const nav_events = document.getElementById('nav-events');
    nav_create_event.classList.toggle('disabled');
    nav_events.classList.toggle('disabled');
    resetEvents();
}