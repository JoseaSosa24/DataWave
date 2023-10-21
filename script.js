var swiper = new Swiper(".mySwiper", {
  direction: "horizontal",
  loop: true,
  autoplay: {
    delay: 10000,
    pauseOnMouseEnter: true,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// Back to top button
$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
    $(".back-to-top").fadeIn("slow");
  } else {
    $(".back-to-top").fadeOut("slow");
  }
});
$(".back-to-top").click(function () {
  $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
  return false;
});
function cambiarTema() {
  const body = document.querySelector("body");
  const themeIcon = document.getElementById("theme-icon");
  if (body.getAttribute("data-bs-theme") === "light") {
    body.setAttribute("data-bs-theme", "dark");
    body.classList.add("dark-mode");
    themeIcon.classList.remove("bi-moon-fill");
    themeIcon.classList.add("bi-sun-fill");
    themeIcon.setAttribute("title", "Modo claro");
  } else {
    body.setAttribute("data-bs-theme", "light");
    body.classList.remove("dark-mode");
    themeIcon.classList.remove("bi-sun-fill");
    themeIcon.classList.add("bi-moon-fill");
    themeIcon.setAttribute("title", "Modo oscuro");
  }
}
