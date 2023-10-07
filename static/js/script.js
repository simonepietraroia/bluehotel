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

/* booking form check-out and check-in dates */

var currentDateTime = new Date();
var year = currentDateTime.getFullYear();
var month = (currentDateTime.getMonth() + 1);
var date = (currentDateTime.getDate() + 1);

if(date < 10) {
  date = '0' + date;
}
if(month < 10) {
  month = '0' + month;
}

var dateTomorrow = year + "-" + month + "-" + date;
var checkinElem = document.querySelector("#checkin-date");
var checkoutElem = document.querySelector("#checkout-date");

checkinElem.setAttribute("min", dateTomorrow);

checkinElem.onchange = function () {
    checkoutElem.setAttribute("min", this.value);
}


