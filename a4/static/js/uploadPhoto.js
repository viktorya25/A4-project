document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file-upload");
    const previewImage = document.getElementById("preview");
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (!file) return;

        if (file.size > 5 * 1024 * 1024) {
            alert("Файл слишком большой. Максимальный размер - 5MB.");
            return;
        }

        // Показ превью
        const reader = new FileReader();
        reader.onload = function (e) {
            previewImage.src = e.target.result;
        };
        reader.readAsDataURL(file);

        // Отправка на сервер
        const formData = new FormData();
        formData.append("avatar", file);
        
        fetch("/users/profile/", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => Promise.reject(err));
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                console.log("Аватар успешно обновлён");
                if (data.avatar_url) {
                    previewImage.src = data.avatar_url;
                }
            } else {
                console.error("Ошибка:", data.errors);
                alert("Ошибка при загрузке аватара: " + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error("Ошибка при сохранении аватара:", error);
            alert("Произошла ошибка при загрузке аватара");
        });
    });
});