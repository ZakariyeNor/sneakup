// Wait until the full HTML document is loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  
  // Select all forms with the class 'qty-update-form' (one per cart item)
  document.querySelectorAll('.qty-update-form').forEach(form => {
    
    // Find the decrement (minus) button inside this form
    const decrementBtn = form.querySelector('.btn-decrement');
    // Find the increment (plus) button inside this form
    const incrementBtn = form.querySelector('.btn-increment');
    // Find the input that holds the quantity value inside this form
    const qtyInput = form.querySelector('.qty-input');
    // Find the trash (remove) button inside this form
    const trashBtn = form.querySelector('.btn-trash');

    // Function to update button visibility and enable/disable states based on current qty
    function updateUI() {
      // Parse the quantity input value as an integer number
      const qty = parseInt(qtyInput.value);

      // Show the trash button if qty is 1 or less, otherwise hide it
      trashBtn.style.display = (qty <= 1) ? 'inline-block' : 'none';

      // Show the decrement button if qty is 2 or more, otherwise hide it
      decrementBtn.style.display = (qty >= 2) ? 'inline-block' : 'none';

      // Disable decrement button if qty is 1 or less (can't go lower)
      decrementBtn.disabled = qty <= 1;
      // Disable increment button if qty is 10 or more (max limit)
      incrementBtn.disabled = qty >= 10;
    }

    // When the decrement button is clicked
    decrementBtn.addEventListener('click', () => {
      // Get the current quantity as a number
      let qty = parseInt(qtyInput.value);
      // Only decrement if qty is greater than 1
      if (qty > 1) {
        // Decrease the quantity by 1
        qtyInput.value = qty - 1;
        // Update the UI buttons accordingly
        updateUI();
        // Submit the form programmatically to update the server
        form.requestSubmit();
      }
    });

    // When the increment button is clicked
    incrementBtn.addEventListener('click', () => {
      // Get the current quantity as a number
      let qty = parseInt(qtyInput.value);
      // Only increment if qty is less than 10
      if (qty < 10) {
        // Increase the quantity by 1
        qtyInput.value = qty + 1;
        // Update the UI buttons accordingly
        updateUI();
        // Submit the form programmatically to update the server
        form.requestSubmit();
      }
    });

    // When the trash button is clicked (to remove the item)
    trashBtn.addEventListener('click', () => {
      // Set quantity to 0 to indicate removal
      qtyInput.value = 0;
      // Update the UI buttons accordingly
      updateUI();
      // Submit the form programmatically to update the server and remove the item
      form.requestSubmit();
    });

    // Initial call to set the correct button states on page load
    updateUI();
  });
});