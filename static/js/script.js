document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-menu");
    const menuContainer = document.querySelector(".menu-container");
    const overlay = document.getElementById("overlay");

    toggleButton.addEventListener("click", function () {
        menuContainer.style.left = menuContainer.style.left === "0px" ? "-250px" : "0px";
        overlay.style.width = overlay.style.width === "100%" ? "0" : "100%";
    });

    overlay.addEventListener("click", function () {
        menuContainer.style.left = "-250px";
        overlay.style.width = "0";
    });
});