function goBackHome() {
    window.location.href = "{{ url_for('back_to_home') }}";
}

function activateButton(button) {
    console.log('activate');
    // Alle Buttons in der Gruppe deaktivieren
    var buttons = document.querySelectorAll('.Nav_Btn');
    buttons.forEach(function(btn) {
        btn.classList.remove('active');
    });
    
    // Den geklickten Button aktivieren
    button.classList.add('active');
}