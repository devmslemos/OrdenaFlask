const menuHamburger = document.querySelector(".menu-hamburger");
const navLinks = document.querySelector(".nav-links");
const authButtons = document.querySelector(".auth-buttons");

menuHamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    authButtons.classList.toggle('active'); 
    menuHamburger.classList.toggle('active');
});