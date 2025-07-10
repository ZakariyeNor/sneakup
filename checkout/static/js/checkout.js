// Get stripe public key and stripe secret key
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var stripe_secret_key = $('#id_client_secret').text().slice(1, -1);
// Set up stripe
var stripe = Stripe(stripe_public_key);
// Now using stripe create instance of stripe elements
var elements = stripe.elements();

// Style the card fields and it's inputs 
var style = {
  base: {
    fontFamily: "'Open Sans', sans-serif",
    fontSize: '16px',
    color: '#000000',
    '::placeholder': {
      color: '#888888',
    },
  },
  invalid: {
    color: '#ff4c60',
  }
};

// Use that elements to create a card elements
var cardNumber = elements.create("cardNumber", { style: style });
var cardExpiry = elements.create("cardExpiry", { style: style });
var cardCvc = elements.create("cardCvc", { style: style });

// Mount them to DOM or elements by their id
cardNumber.mount("#card-number-element");
cardExpiry.mount("#card-expiry-element");
cardCvc.mount("#card-cvc-element");

/* Validation errors on the card number, date and cvc
 and showing them by field */

function showErrorByField(event, elementId) {
  const errorSpan = document.getElementById(elementId);
  if (event.error) {
    errorSpan.innerHTML = `
      <span class="text-danger" role="alert">
        <i class="fas fa-times me-1"></i>
        ${event.error.message}
      </span>
    `;
    errorSpan.classList.remove('d-none')
  } else {
    errorSpan.textContent = '';
    errorSpan.classList.add('d-none')
  }
}

// Then attach event listeners to each Stripe Element
cardNumber.on('change', (event) => showErrorByField(event, 'card-number-error-display'));
cardExpiry.on('change', (event) => showErrorByField(event, 'card-expiry-error-display'));
cardCvc.on('change', (event) => showErrorByField(event, 'card-cvc-error-display'));

/* Display global card errors unrelated
 to specific fields */
function showGlobalCardError(message) {
  const globalError = document.getElementById('card-errors-display');
  if (message) {
    globalError.innerHTML = `
      <span class="text-danger" role="alert">
        <i class="fas fa-times me-1"></i>
        ${message}
      </span>
    `;
    globalError.classList.remove('d-none');
  } else {
    globalError.textContent = '';
    globalError.classList.add('d-none');
  }
}


