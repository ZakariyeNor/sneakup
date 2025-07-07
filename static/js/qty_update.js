// Wait until the full HTML document is loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  
  // Process each quantity update form (one per cart item)
  document.querySelectorAll('.qty-update-form').forEach(form => {
    
    // Get buttons and input fields for quantity control inside the current form
    const decrementBtn = form.querySelector('.btn-decrement');
    const incrementBtn = form.querySelector('.btn-increment');
    const qtyInput = form.querySelector('.qty-input');
    const trashBtn = form.querySelector('.btn-trash');

    // Update visibility and enabled/disabled state of buttons based on current quantity
    function updateUI() {
      const qty = parseInt(qtyInput.value);

      // Toggle trash and decrement buttons visibility and enable/disable states based on qty limits
      trashBtn.style.display = (qty <= 1) ? 'inline-block' : 'none';
      decrementBtn.style.display = (qty >= 2) ? 'inline-block' : 'none';
      decrementBtn.disabled = qty <= 1;
      incrementBtn.disabled = qty >= 10;
    }

    // Handle decrement button click: reduce quantity, update UI, and submit form
    decrementBtn.addEventListener('click', () => {
      let qty = parseInt(qtyInput.value);
      if (qty > 1) {
        qtyInput.value = qty - 1;
        updateUI();
        form.requestSubmit();
      }
    });

    // Handle increment button click: increase quantity, update UI, and submit form
    incrementBtn.addEventListener('click', () => {
      let qty = parseInt(qtyInput.value);
      if (qty < 10) {
        qtyInput.value = qty + 1;
        updateUI();
        form.requestSubmit();
      }
    });

    // Handle trash button click: set quantity to zero, update UI, and submit form to remove item
    trashBtn.addEventListener('click', () => {
      qtyInput.value = 0;
      updateUI();
      form.requestSubmit();
    });

    // Initialize UI button states on page load
    updateUI();
  });
});
