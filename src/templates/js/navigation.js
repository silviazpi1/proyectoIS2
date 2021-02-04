var navigation = document.getElementsByClassName("navElement");
var isMenuOpen = false;

function setCurrentPage(index) {
    navigation[index].classList.add("aCurrent");
}

function toggleMenu() {
    if (isMenuOpen === false) {
        document.querySelector("header#hdrMain nav.navMenu").style.display = "block";
    } else {
        document.querySelector("header#hdrMain nav.navMenu").style.display = "none";
    }

    isMenuOpen = !isMenuOpen;
}