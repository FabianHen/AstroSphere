function goBackHome() {
    window.location.href = '/';
}

function goToShop(element) {
    window.location.href += `/shop?selected=${element}`;
}

document.addEventListener("DOMContentLoaded", function() {
    var advertisement = document.getElementById("advertisement");
    var adImage = document.getElementById("adImage");
    var imageSources = [
        "../static/images/advertisement_1.png",
        "../static/images/advertisement_2.png",
        "../static/images/advertisement_3.png"
    ];
    var currentIndex = 0;
    var intervalId;

    function showNextImage() {
        currentIndex = (currentIndex + 1) % imageSources.length;
        adImage.src = imageSources[currentIndex];
    }

    function startInterval() {
        intervalId = setInterval(function() {
            showNextImage();
            advertisement.style.display="flex";
        }, 7000);
    }

    document.addEventListener("click", reset);
    function reset(){
        advertisement.style.display="none";
        clearInterval(intervalId);
        setTimeout(startInterval, 15000);
    }

    reset();
});
