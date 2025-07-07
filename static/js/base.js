// Wait for the full HTML document to be loaded
document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    /* ============================
       Mobile menu toggle functionality
       Toggles the visibility of mobile navigation menu
    ============================= */
    const burgerIcon = document.querySelector('.menu-icon');
    const listItems = document.querySelector('.mobile-nav');

    // Only add event listener if both elements exist on the page
    if (burgerIcon && listItems) {
        burgerIcon.addEventListener('click', function () {
            // Toggle 'open' class to show/hide the mobile menu
            listItems.classList.toggle('open');
        });
    }

    /* ============================
       Search icon toggle functionality
       Shows or hides the search form on clicking search icon
    ============================= */
    const searchToggle = document.getElementById('searchToggle');
    const searchForm = document.getElementById('searchFormContainer');

    if (searchToggle && searchForm) {
        searchToggle.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent default action
            searchForm.classList.toggle('d-none');

            // If search form is now visible, set focus to the input field inside it
            if (!searchForm.classList.contains('d-none')) {
                const input = searchForm.querySelector('input[name="q"]');
                if (input) input.focus();
            }
        });
    }

    /* ============================
       Size boxes selection functionality
       Lets user select product size; updates hidden input accordingly
    ============================= */
    const sizeBoxes = document.querySelectorAll('.size-box');
    const selectedSize = document.getElementById('selectedSizeInput');

    // Only proceed if size boxes exist and hidden input is present
    if (sizeBoxes && selectedSize) {
        sizeBoxes.forEach(box => {
            box.addEventListener('click', function () {
                // Remove 'selected' class from all size boxes to clear previous selection
                sizeBoxes.forEach(b => b.classList.remove('selected'));
                // Add 'selected' class to the clicked size box
                this.classList.add('selected');

                // Update the hidden input value to the selected size (from data attribute)
                selectedSize.value = this.dataset.size;

                // Log the selected size for debugging purposes
                console.log('Selected size:', this.dataset.size);
            });
        });
    }

    /* ============================
       Quantity increment and decrement controls
       Manage product quantity input with max and min restrictions
    ============================= */
    const quantity = document.getElementById('quantity');
    const incrementBtn = document.getElementById('increment-btn');
    const decrementBtn = document.getElementById('decrement-btn');

    if (quantity && incrementBtn && decrementBtn) {
        // Increase quantity by 1, but not above max attribute value
        incrementBtn.addEventListener('click', function () {
            const max = parseInt(quantity.max);
            let current = parseInt(quantity.value);
            if (current < max) quantity.value = current + 1;

            // Log new quantity value for debugging
            console.log('quantity:', quantity.value);
        });

        // Decrease quantity by 1, but not below min attribute value
        decrementBtn.addEventListener('click', function () {
            const min = parseInt(quantity.min);
            let current = parseInt(quantity.value);
            if (current > min) quantity.value = current - 1;

            // Log new quantity value for debugging
            console.log('quantity:', quantity.value);
        });
    }

});
