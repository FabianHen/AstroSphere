/**
 * Sends the User back to the homescreen
 */
function goBackHome() {
    window.location.href = '/';
}

/**
 * Sends the User to the Shop screen
 * @param element the filter that is set in the shop
 */
function goToShop(element) {
    window.location.href += `/shop?selected=${element}`;
}

/**
 * Sends the User to the Directions screen
 */
function goToDirections() {
    window.location.href += `/directions`;
}

document.addEventListener("DOMContentLoaded", function () {
    var advertisement = document.getElementById("advertisement");
    var adImage = document.getElementById("adImage");
    var imageSources = [
        "../static/images/advertisement_1.png",
        "../static/images/advertisement_2.png",
        "../static/images/advertisement_3.png"
    ];
    var currentIndex = 0;
    var intervalId;

    /**
     * Changes the current ad to the next one
     */
    function showNextImage() {
        currentIndex = (currentIndex + 1) % imageSources.length;
        adImage.src = imageSources[currentIndex];
    }

    /**
     * Displays an ad and changes it every 7 seconds
     */
    function startInterval() {
        intervalId = setInterval(function () {
            showNextImage();
            advertisement.style.display = "flex";
        }, 7000);
    }

    document.addEventListener("click", reset);
    /**
     * Removes the ad from the screen and shows it again after 15seconds of inactivity
     */
    function reset() {
        advertisement.style.display = "none";
        clearInterval(intervalId);
        setTimeout(startInterval, 15000);
    }

    reset();
});
