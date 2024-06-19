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
    else{
        document.getElementById('errorLogin').style.display="block";
    }
}






function goToStart(){
    document.getElementById('impressum').style.display="none";
    document.getElementById('aboutUs').style.display="none";
    document.getElementById('startpage').style.display="block";
}
function goToAboutUs(){
    document.getElementById('impressum').style.display="none";
    document.getElementById('startpage').style.display="none";
    document.getElementById('aboutUs').style.display="block";
}
function goToImpressum(){
    document.getElementById('aboutUs').style.display="none";
    document.getElementById('startpage').style.display="none";
    document.getElementById('impressum').style.display="block";
}








function goToTerminal() {
    window.location.href = "/terminal";
}

function goToIntern() {
    showLogInPage();
}