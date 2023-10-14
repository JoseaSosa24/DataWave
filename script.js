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
})