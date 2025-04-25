const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    // Toggle 'active' class on hamburger icon
    hamburger.classList.toggle("active");
    // Toggle 'active' class on navigation menu
    navMenu.classList.toggle("active");
});

// Optional: Close menu when a link is clicked
document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
        // Only close if the menu is actually open (on mobile view)
        if (hamburger.classList.contains("active")) {
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
        }
    });
});