/*  Toggle Script */
document.addEventListener('DOMContentLoaded', function() {
    /* Mobile menu toggle */
    const burgerIcon = document.querySelector('.menu-icon');
    const listItems = document.querySelector('.mobile-nav');

    const searchToggle = document.getElementById('searchToggle');
    const searchForm = document.getElementById('searchFormContainer');

    if(burgerIcon && listItems) {
        burgerIcon.addEventListener('click', function() {
            listItems.classList.toggle('open')
        });
    }

    searchToggle.addEventListener('click', function(e) {
        e.preventDefault();
        searchForm.classList.toggle('d-none');
        if (!searchForm.classList.contains('d-none')) {
        // Focus input when shown
        const input = searchForm.querySelector('input[name="q"]');
        if (input) input.focus();
      }
    });
});