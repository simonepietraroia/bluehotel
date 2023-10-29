function toggleMenu(menuContainer, overlay) {
  menuContainer.style.left = menuContainer.style.left === "0px" ? "-250px" : "0px";
  overlay.style.width = overlay.style.width === "100%" ? "0" : "100%";
}

function closeMenu(menuContainer, overlay) {
  menuContainer.style.left = "-250px";
  overlay.style.width = "0";
}

document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("toggle-menu");
  const menuContainer = document.querySelector(".menu-container");
  const overlay = document.getElementById("overlay");

  toggleButton.addEventListener("click", function () {
      toggleMenu(menuContainer, overlay);
  });

  overlay.addEventListener("click", function () {
      closeMenu(menuContainer, overlay);
  });
});

module.exports = {
  toggleMenu,
  closeMenu,
};
