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
