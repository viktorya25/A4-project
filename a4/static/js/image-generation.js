document.addEventListener('DOMContentLoaded', function() {
    const ratioButtons = document.querySelectorAll('.ratio-btn');
    const generateBtn = document.querySelector('.image-generate-btn');
    const descriptionField = document.querySelector('.idea-description');
    const generatedImagesContainer = document.querySelector('.generated-images');
    const placeholder = document.querySelector('.results-placeholder');

    let selectedRatio = '1:1';

    // Выбор соотношения сторон
    ratioButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            ratioButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selectedRatio = this.textContent;
        });
    });

    // Генерация изображений
    generateBtn.addEventListener('click', async function() {
        const prompt = descriptionField.value.trim();
        
        if (!prompt) {
            alert('Пожалуйста, введите описание идеи');
            return;
        }

        // Показываем загрузку
        placeholder.style.display = 'none';
        generatedImagesContainer.innerHTML = '<div class="loading">Генерация изображения...</div>';
        
        // Блокируем кнопку на время генерации
        generateBtn.disabled = true;
        generateBtn.textContent = 'Генерация...';
        
        try {
            const response = await fetch('/projects/generate-image/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    prompt: prompt,
                    ratio: selectedRatio
                })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                displayGeneratedImage(data.image);
            } else {
                throw new Error(data.message || 'Ошибка генерации');
            }
        } catch (error) {
            generatedImagesContainer.innerHTML = `
                <div class="error-message">
                    Ошибка: ${error.message}
                    <button onclick="window.location.reload()">Попробовать снова</button>
                </div>
            `;
            console.error('Generation error:', error);
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = 'Сгенерировать';
        }
    });

    function displayGeneratedImage(imageBase64) {
        generatedImagesContainer.innerHTML = '';
        
        const imgContainer = document.createElement('div');
        imgContainer.className = 'generated-image-container';
        
        const imgElement = document.createElement('img');
        imgElement.className = 'generated-image';
        imgElement.src = `data:image/jpeg;base64,${imageBase64}`;
        imgElement.alt = 'Сгенерированное изображение';
        
        // Кнопка скачивания
        const downloadBtn = document.createElement('button');
        downloadBtn.className = 'download-btn';
        downloadBtn.textContent = 'Скачать';
        downloadBtn.addEventListener('click', () => {
            const link = document.createElement('a');
            link.href = imgElement.src;
            link.download = `generated-image-${new Date().getTime()}.jpg`;
            link.click();
        });
        
        imgContainer.appendChild(imgElement);
        imgContainer.appendChild(downloadBtn);
        generatedImagesContainer.appendChild(imgContainer);
    }

    // Вспомогательная функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});