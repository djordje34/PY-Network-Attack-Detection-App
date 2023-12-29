from django.shortcuts import render
from django.http import JsonResponse
from wrapper import Wrapper
# Create your views here.

def index(request):
    return render(request, 'detector/index.html')

def predict(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        
        wrapper = Wrapper()
        pred = wrapper.predict(data)
        return JsonResponse({'prediction': pred})
    else:
        return JsonResponse({'error': 'Invalid request method'})