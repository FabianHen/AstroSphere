function goBack() {
    window.location.href = window.location.href.split('/', window.location.href.split('/').length-1).join('/');
}





function cancel_Order(){
    console.log("cancel Order");
}
function buy_Order(){
    console.log("buy Order");
}