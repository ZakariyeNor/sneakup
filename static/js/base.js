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

    const quantity = document.getElementById('quantity');
    const incrementBtn = document.getElementById('increment-btn');
    const decrementBtn = document.getElementById('decrement-btn');

    incrementBtn.addEventListener('click', function(e) {
        e.preventDefault();
        const max = parseInt(quantity.max);
        let current = parseInt(quantity.value);
        if (current < max) quantity.value = current + 1;
    })

    decrementBtn.addEventListener('click', function(e) {
        e.preventDefault
        const min = parseInt(quantity.min);
        let current = parseInt(quantity.value);
        if (current > min) quantity.value = current - 1;
    })

    console.log('Selected size:', this.dataset.size);
    console.log('quantity:', current);

    /* Increment the specific item in the shopping bag, to attach click listeners to all increment buttons */
    document.querySelectorAll('button[id^="increment-qty-btn"]').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            console.log('Clicked:', event.target.id);
            /* Get the id from the event or the product */
            const productId = event.target.id.split('-').pop();
            console.log('Product ID:', productId);
            const qtyInput = document.getElementById(`qty-input-${productId}`);
            console.log('Quantity Input:', qtyInput);
            /* Get the maximum value from the input value */
            const max = parseInt(qtyInput.max);
            const currentQty = parseInt(qtyInput.value);
            if (currentQty < max) {
                qtyInput.value = currentQty + 1;
            }

        });
    });

    /* Decrement the specific item in the shopping bag, to attach click listeners to all decrement buttons */
    document.querySelectorAll('button[id^="decrement-qty-btn"]').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            console.log('Clicked:', event.target.id);
            const productId = event.target.id.split('-').pop();
            console.log('Product ID:', productId);
            const qtyInput = document.getElementById(`qty-input-${productId}`);
            console.log('Quantity Input:', qtyInput);
            const min = parseInt(qtyInput.min);
            const currentQty = parseInt(qtyInput.value);
            if (currentQty > min) {
                qtyInput.value = currentQty - 1;
            }
        });
    });
});