const form = document.querySelector("#filter-form");
const btnFilter = document.querySelector("#filter-books");

btnFilter.addEventListener('click', () => {
    form.submit()
})

const add_modal = document.querySelector("#add-modal");
const btn_add_modal = document.querySelector("#adicionar-livro");
const overlay = document.querySelector("#add-overlay");

btn_add_modal.addEventListener('click', () => {
    add_modal.classList.remove('deactivated')
    overlay.classList.remove('deactivated');
})

const close_add_form = document.querySelector("#close-add-form");

close_add_form.addEventListener("click", () => {
    add_modal.classList.add("deactivated");
    overlay.classList.add("deactivated");
})

const clear_filter = document.querySelector("#clear-filter-books");

clear_filter.addEventListener('click', () => {
    filters_input = document.querySelectorAll(".filter input");
    document.querySelector(".filter select").value = null;
    console.log(filters_input);
    filters_input.forEach(element => {
        element.value = null
    });
})
    