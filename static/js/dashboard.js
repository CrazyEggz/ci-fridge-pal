let deleteItemModal = document.getElementById('deleteItemModal');

deleteItemModal.addEventListener('show.bs.modal', function (event) {
  let button = event.relatedTarget;
  let deleteItemUrl = button.getAttribute('data-bs-delete-url');
  let deleteItemName = button.getAttribute('data-bs-item-name');
  let modalDeleteButton = deleteItemModal.querySelector('#model-delete-btn');
  let modalTitle = deleteItemModal.querySelector('.modal-title')

  modalDeleteButton.action = deleteItemUrl;
  modalTitle.textContent = `Are you sure you want to delete the item ${deleteItemName}?`
});
