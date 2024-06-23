function goBackHome() {
    window.location.href = '/';
}

function goToShop(element) {
    // window.location.href = `/shop/${element.id}`;
    window.location.href += '/shop';
}