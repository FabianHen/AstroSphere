document.addEventListener("DOMContentLoaded", function(){
    getRooms();
});

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

function goToRooms() {
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


function processRooms(data) {
    var products = document.getElementById('roomTable');
    var tempHTML = '';

    products.innerHTML = '';

    data.forEach(raum => {
        let status = "frei";
        if(raum.PREIS== NULL){
            status == "Abteilungsraum";
        }
            tempHTML += `
                <tr>
                    <td class="roomName">${raum.BEZEICHNUNG}</td>
                    <td>${raum.ID}</td>
                    <td>${raum.KAPAZITÄT}</td>
                    <td class="${status}">${status}</td>
                </tr>`;
        }
    );

    products.innerHTML = tempHTML;
}