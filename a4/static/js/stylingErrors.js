document.addEventListener('DOMContentLoaded', function() {
    const errorFields = document.querySelectorAll('.errorlist');

    errorFields.forEach(function(errorField) {
        const inputField = errorField.previousElementSibling;

        if (inputField && inputField.tagName === 'INPUT') {
            inputField.classList.add('error');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.form input');

    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            if (input.classList.contains('error')) {
                input.classList.remove('error');
                const errorList = input.nextElementSibling;
                if (errorList && errorList.classList.contains('errorlist')) {
                    errorList.remove();
                }
            }
        });
    });
});