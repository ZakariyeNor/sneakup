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

    const sizeBoxes = document.querySelectorAll('.size-box')
    const selectedSize = document.getElementById('selectedSizeInput')

    sizeBoxes.forEach(box => {
        box.addEventListener('click', function(e) {
            sizeBoxes.forEach(b => b.classList.remove('selected'));
            this.classList.add('selected');

            selectedSize.value = this.dataset.size
        });
    });

    console.log('Selected size:', this.dataset.size);

});