import json
from django.shortcuts import render
from django.http import JsonResponse
from apps.detector.wrapper import Wrapper
from apps.detector.preprocess_pipeline import PreprocessPipeline
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.shortcuts import render

def show_form(request):
    return render(request, 'forms.html')

def index(request):
    response = render(request, 'index.html')

    return response


def process_form(request):
    if request.method == 'POST':
        return render(request, 'success_page.html')
    return render(request, 'forms.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body.decode('utf-8'))
            wrapper = Wrapper()
            data = PreprocessPipeline.preprocessData(data)
            pred = wrapper.predict(data)
            pred_list = pred.tolist()
            return JsonResponse({'prediction': pred_list})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in the request body'}, status=400)

    else:
        return JsonResponse({'error':'Something went wrong'}, status = 405)