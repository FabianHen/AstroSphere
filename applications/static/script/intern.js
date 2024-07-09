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
        loadMedia(mediaItem);
    }
});

function loadMedia(elem) {
    // Datenbank lesen
    let medien = getMedium();
    
    medien.forEach(medium => {
        var htmlElem =  "<a href='#' class='media-item' onclick='mediaPressed(this)'>"
        htmlElem += "<img src=" + medium.IMAGE_PATH + " alt='Media 1'>"
        if(medium.GALAXIE.NAME) {
            htmlElem += "<h3>" + medium.GALAXIE.NAME + "</h3>"
        }
        if(medium.PLANET.NAME) {
            htmlElem += "<h3>" + medium.PLANET.NAME + "</h3>"
        }
        if(medium.STERN.NAME) {
            htmlElem += "<h3>" + medium.STERN.NAME + "</h3>"
        }
        if(medium.NEBEL.NAME) {
            htmlElem += "<h3>" + medium.NEBEL.NAME + "</h3>"
        }
        if(medium.STERNENBILD.NAME) {
            htmlElem += "<h3>" + medium.STERNENBILD.NAME + "</h3>"
        }
        if(medium.PLANETENSYSTEM.NAME) {
            htmlElem += "<h3>" + medium.PLANETENSYSTEM.NAME + "</h3>"
        }
        if(medium.KOMET.NAME) {
            htmlElem += "<h3>" + medium.KOMET.NAME + "</h3>"
        }

        htmlElem += "<p>" + medium.FORMAT + "</p>"
        htmlElem += "</a>"

        elem.innerHTML += htmlElem;
    });
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

async function getMedium() {
    try {
        const response = await fetch('/intern/events/medien');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
  
        return data;
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