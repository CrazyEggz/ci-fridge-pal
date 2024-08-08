// Initialise popovers
document.querySelectorAll('[data-bs-toggle="popover"]')
  .forEach(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));


let deleteItemModal = document.getElementById('deleteItemModal');
deleteItemModal.addEventListener('show.bs.modal', function (event) {
  let button = event.relatedTarget;

  let modalDeleteButton = deleteItemModal.querySelector('#model-delete-btn');
  let deleteItemUrl = button.getAttribute('data-bs-delete-url');
  modalDeleteButton.action = deleteItemUrl;

  let modalTitle = deleteItemModal.querySelector('.modal-title');
  let deleteItemName = button.getAttribute('data-bs-item-name');
  modalTitle.textContent = `Are you sure you want to delete the item ${deleteItemName}?`;
});


/**
 * Set the URL parameter when the button is clicked.
 */
function onParameterButtonClick(event) {
  let parameterKey = event.target.getAttribute('data-parameter-key');
  let parameterValue = event.target.getAttribute('data-parameter-value');
  let params = new URLSearchParams(window.location.search);
  params.set(parameterKey, parameterValue);
  window.location.search = params.toString();
}

// Set up parameter buttons
const parameterButtons = document.getElementsByClassName('parameter-btn')
for (let button of parameterButtons) {
  button.addEventListener('click', onParameterButtonClick);
}
