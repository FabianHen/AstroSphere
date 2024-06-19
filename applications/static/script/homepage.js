function showLogInPage(){
    document.getElementById('loginpage').style.display="block";
}
function hideLogInPage(){
    document.getElementById('loginpage').style.display="none";
    document.getElementById('username').value="";
    document.getElementById('password').value="";
}
function login(event){
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log("try to login with user: "+username+", and password: "+password);
    if(username=="admin" && password=="admin"){
        window.location.href = "/intern";
    }
}






function goToStart(){
    console.log("go to start");
}
function goToAboutUs(){
    document.getElementById('aboutUs').style.display="block";
}
function goToImpressum(){
    console.log("go to impressum");
}








function goToTerminal() {
    window.location.href = "{{ url_for('terminal') }}";
}

function goToIntern() {
    showLogInPage();
}