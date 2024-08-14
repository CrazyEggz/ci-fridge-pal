'use strict';

// Initialise popovers
document.querySelectorAll('[data-bs-toggle="popover"]')
  .forEach(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));


const deleteItemModal = document.getElementById('deleteItemModal');
deleteItemModal.addEventListener('show.bs.modal', function (event) {
  const button = event.relatedTarget;

  const modalDeleteButton = deleteItemModal.querySelector('#model-delete-btn');
  const deleteItemUrl = button.getAttribute('data-bs-delete-url');
  modalDeleteButton.action = deleteItemUrl;

  const modalTitle = deleteItemModal.querySelector('.modal-title');
  const deleteItemName = button.getAttribute('data-bs-item-name');
  modalTitle.textContent = `Are you sure you want to delete the item ${deleteItemName}?`;
});


/**
 * Set the URL parameter when the button is clicked.
 */
function onParameterButtonClick(event) {
  const parameterKey = event.target.getAttribute('data-parameter-key');
  const parameterValue = event.target.getAttribute('data-parameter-value');
  const params = new URLSearchParams(window.location.search);
  params.set(parameterKey, parameterValue);
  window.location.search = params.toString();
}

// Set up parameter buttons
const parameterButtons = document.getElementsByClassName('parameter-btn');
for (const button of parameterButtons) {
  button.addEventListener('click', onParameterButtonClick);
}

const tableRows = document.querySelectorAll('#fridge-table > tbody > tr');
for (const row of tableRows) {
  row.addEventListener('click', () => row.classList.toggle("active"));
}