const pesquisaIcone = document.getElementById('search-icon');
const pesquisaInput = document.getElementById('search-input');

pesquisaIcone.addEventListener('click', function () {
    pesquisaInput.classList.toggle('active');
    if (pesquisaInput.classList.contains('active')) {
        pesquisaInput.focus();
    } else {
        pesquisaInput.blur();
    }
});