function toggleAccordion(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.accordion-icon');

    if (content.style.maxHeight) {
      // Accordion is open, close it
      content.style.maxHeight = null;
      content.classList.remove('open');
      icon.classList.remove('rotate');
    } else {
      // Close all other accordions
      document.querySelectorAll('.accordion-content').forEach(c => {
        c.style.maxHeight = null;
        c.classList.remove('open');
      });
      document.querySelectorAll('.accordion-icon').forEach(i => {
        i.classList.remove('rotate');
      });

      // Open this one
      content.style.maxHeight = content.scrollHeight + "px";
      content.classList.add('open');
      icon.classList.add('rotate');
    }
  }

  // Optional: Open first FAQ on page load
  document.addEventListener('DOMContentLoaded', () => {
    const firstHeader = document.querySelector('.accordion-header');
    if (firstHeader) {
      toggleAccordion(firstHeader);
    }
  });