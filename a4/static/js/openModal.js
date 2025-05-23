const modal = document.getElementById("ModalWindow");
const openModalBtn = document.getElementById("openModalWindow");
const closeModalBtn = document.querySelector(".close");

openModalBtn.addEventListener("click", function () {
    modal.style.display = "block";
});

closeModalBtn.addEventListener("click", function () {
    modal.style.display = "none";
});

window.addEventListener("click", function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});