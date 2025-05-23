document.addEventListener('DOMContentLoaded', function() {
    let alerts = document.querySelectorAll('.messages .alert');

    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade-out');

            alert.addEventListener('animationend', function() {
                alert.remove();
            });
        }, 3000); // Время до исчезновения (5 секунд)
    });
});