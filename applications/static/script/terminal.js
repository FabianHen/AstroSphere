function goBackHome() {
    window.location.href = '/';
}

function goToShop(element) {
    window.location.href += `/shop?selected=${element}`;
}