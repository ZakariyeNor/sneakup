document.addEventListener('DOMContentLoaded', function () {
    const country = document.getElementById('id_default_country');

    if (!country.value) {
        country.style.color = '#888888';  // Placeholder style
    } else {
        country.style.color = '#000000';  // Selected value
    }

    // Uupdate color when user changes country
    country.addEventListener('change', function () {
        if (!country.value) {
            country.style.color = '#888888';
        } else {
            country.style.color = '#000000';
        }
    });
});
