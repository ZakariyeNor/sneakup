// Get stripe public key and stripe secret key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
console.log("clientSecret:", clientSecret);

// Set up stripe
var stripe = Stripe(stripePublicKey);
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

// Handle form submit
const form = document.getElementById('payment-form');

// Listen for the form submission
form.addEventListener('submit', function (event) {
  event.preventDefault();

  // Disable UI
  cardNumber.update({ disabled: true });
  cardExpiry.update({ disabled: true });
  cardCvc.update({ disabled: true });
  // Get the submit button and disable it
  const submitButton = document.getElementById('submit-button');
  submitButton.disabled = true;
  submitButton.textContent = 'Processing...';

  console.log('Calling confirmCardPayment…');
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: cardNumber,
      billing_details: {
        name: document.getElementById('id_first_name').value.trim() + ' ' +
          document.getElementById('id_last_name').value.trim(),
        email: document.getElementById('id_email').value.trim(),
        phone: document.getElementById('id_phone_number').value.trim(),
        address: {
          line1: document.getElementById('id_street_address_1').value.trim(),
          line2: document.getElementById('id_street_address_2').value.trim(),
          city: document.getElementById('id_city').value.trim(),
          postal_code: document.getElementById('id_postcode').value.trim(),
          country: document.getElementById('id_country').value.trim(),
        }
      }
    },
    shipping: {
      name: document.getElementById('id_first_name').value.trim() + ' ' +
        document.getElementById('id_last_name').value.trim(),
      phone: document.getElementById('id_phone_number').value.trim(),
      address: {
        line1: document.getElementById('id_street_address_1').value.trim(),
        line2: document.getElementById('id_street_address_2').value.trim(),
        city: document.getElementById('id_city').value.trim(),
        postal_code: document.getElementById('id_postcode').value.trim(),
        state: document.getElementById('id_county').value.trim(),
        country: document.getElementById('id_country').value.trim(),
      }
    },
  })
  .then(function (result) {
    console.log('confirmCardPayment resolved:', result);

    if (result.error) {
      console.error('Payment error:', result.error);

      // Show the error
      showGlobalCardError(result.error.message);

      // Re‑enable submit button
      submitButton.disabled = false;
      submitButton.textContent = 'Pay €…';
      // Re-enable card inputs
      cardNumber.update({ disabled: false });
      cardExpiry.update({ disabled: false });
      cardCvc.update({ disabled: false });

    } else if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
      console.log('PaymentIntent succeeded, submitting form');
      // Clear the error nad submit
      showGlobalCardError('');
      form.submit();
    } else {
      // Unexpected state
      console.warn('Unexpected PaymentIntent status:', result.paymentIntent);
      showGlobalCardError('Unexpected payment status. Please try again.');
      // Re-enable submit button
      submitButton.disabled = false;
      submitButton.textContent = 'Pay €…';
    }
  })
  .catch(function (err) {
    // This catch is rare—only if the network request itself failed
    console.error('ConfirmCardPayment threw an exception:', err);
    showGlobalCardError('Payment failed. Please reload and try again.');

    // Re-anable submit and card inputs
    submitButton.disabled = false;
    submitButton.textContent = 'Pay €…';
    cardNumber.update({ disabled: false });
    cardExpiry.update({ disabled: false });
    cardCvc.update({ disabled: false });
  });
});

