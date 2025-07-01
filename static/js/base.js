/*  Toggle Script */
document.addEventListener('DOMContentLoaded', function () {
    /* Mobile menu toggle */
    const burgerIcon = document.querySelector('.menu-icon');
    const listItems = document.querySelector('.mobile-nav');

    /* Search icon toggle  */
    const searchToggle = document.getElementById('searchToggle');
    const searchForm = document.getElementById('searchFormContainer');

    if (burgerIcon && listItems) {
        burgerIcon.addEventListener('click', function () {
            listItems.classList.toggle('open')
        });
    }

    searchToggle.addEventListener('click', function (e) {
        e.preventDefault();
        searchForm.classList.toggle('d-none');
        if (!searchForm.classList.contains('d-none')) {
            // Focus input when shown
            const input = searchForm.querySelector('input[name="q"]');
            if (input) input.focus();
        }
    });

    //Get the button
    const backToTopBtn = document.getElementById("backToTopBtn");

    // When the user scrolls down 300px from the top of the document, show the button
    window.onscroll = function () { scrollFunction() };

    function scrollFunction() {
        if (document.documentElement.scrollTop > 300) {
            backToTopBtn.style.display = "block";
        } else {
            backToTopBtn.style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top smoothly
    backToTopBtn.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });


    console.log("base.js loaded");

});
