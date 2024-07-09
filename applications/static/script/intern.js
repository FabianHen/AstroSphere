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
    let testMedia = [['Mond', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Erde', '*.png', '../static/images/pictureNotFound.png'],
                     ['Mars', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Jupiter', '*.jpg', '../static/images/pictureNotFound.png'],
                     ['Saturn', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Venus', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Merkur', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Neptun', '*.svg', '../static/images/pictureNotFound.png'],
                     ['Test', '*.svg', '../static/images/pictureNotFound.png']]
    
    for (var i = 0; i < testMedia.length; i++) {
        var htmlElem =  "<a href='#' class='media-item' onclick='mediaPressed(this)'>"
        htmlElem += "<img src=" + testMedia[i][2] + " alt='Media 1'>"
        htmlElem += "<h3>" + testMedia[i][0] + "</h3>"
        htmlElem += "<p>" + testMedia[i][1] + "</p>"
        htmlElem += "</a>"

        elem.innerHTML += htmlElem;
    }
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

function openContent(option) {
    switch (option) {
        case 'planeten':
            // Planeten anzeigen
            break;
        case 'sternenbilder':
            // Sternenbilder anzeigen
            break;
        case 'kometen':
            // Kometen anzeigen
            break;
    }
}
