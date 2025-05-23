import base64
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yandex_cloud_ml_sdk import YCloudML
from django.conf import settings
import random


@csrf_exempt
def generate_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt')
            ratio = data.get('ratio', '1:1')  # По умолчанию 1:1
            
            width_ratio, height_ratio = map(int, ratio.split(':'))
            
            sdk = YCloudML(
                folder_id=settings.YANDEX_FOLDER_ID,
                auth=settings.YANDEX_API_KEY
            )
            
            model = sdk.models.image_generation("yandex-art")
            model = model.configure(
                width_ratio=width_ratio,
                height_ratio=height_ratio,
                seed=random.randint(1, 10000)
            )
            
            # Генерация изображения
            operation = model.run_deferred(prompt)
            result = operation.wait()
            
            # Конвертируем bytes в base64 для передачи через JSON
            image_base64 = base64.b64encode(result.image_bytes).decode('utf-8')
            
            return JsonResponse({
                "status": "success",
                "image": image_base64,
                "format": "jpeg"  # или другой формат, если измените
            })
            
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
    
    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)

def index(request):
    return render(request, 'projects/projects.html')