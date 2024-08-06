let deleteItemModal = document.getElementById('deleteItemModal');

deleteItemModal.addEventListener('show.bs.modal', function (event) {
  let button = event.relatedTarget;
  let deleteItemUrl = button.getAttribute('data-bs-delete-url');
  let modalDeleteButton = deleteItemModal.querySelector('#model-delete-btn');

  modalDeleteButton.action = deleteItemUrl;
});
