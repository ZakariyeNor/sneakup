document.addEventListener('DOMContentLoaded', function () {
    /* Increment the specific item in the shopping bag, to attach click listeners to all increment buttons */
    document.querySelectorAll('button[id^="increment-qty-btn"]').forEach(button => {
        button.addEventListener('click', function (event) {
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