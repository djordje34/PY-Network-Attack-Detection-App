import json
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from apps.detector.wrapper import Wrapper
from apps.detector.preprocess_pipeline import PreprocessPipeline
from django.views.decorators.csrf import csrf_exempt
from apps.detector.recommender import Recommender
from .models import NetworkData
# Create your views here.

from django.shortcuts import render

def show_form(request):
    return render(request, 'forms.html')

def index(request):
    response = render(request, 'index.html')
    return response

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body.decode('utf-8'))
            wrapper = Wrapper()
            data = PreprocessPipeline.preprocessData(data)
            pred = wrapper.predict(data)
            pred_list = pred.item()
            return JsonResponse({'prediction': pred_list})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in the request body'}, status=400)

    else:
        return JsonResponse({'error':'Something went wrong'}, status = 405)
    
    
@csrf_exempt
def diagnose(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            data = PreprocessPipeline.preprocessDataDiag(data)
            rec = Recommender()
            pred = rec.getRecommendations(data)
            pred_str = PreprocessPipeline.inverseLabelEncoding(pred).tolist()
            return JsonResponse({'prediction':pred_str})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in the request body'}, status=400)

    else:
        return JsonResponse({'error':'Something went wrong'}, status = 405)
    
    
@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        try:
            el = NetworkData.objects.order_by('?').first()
            data = {
                'IPV4_SRC_ADDR': el.IPV4_SRC_ADDR,
                'L4_SRC_PORT': el.L4_SRC_PORT,
                'IPV4_DST_ADDR': el.IPV4_DST_ADDR,
                'L4_DST_PORT': el.L4_DST_PORT,
                'PROTOCOL':el.PROTOCOL,
                'L7_PROTO':el.L7_PROTO,
                'IN_BYTES':el.IN_BYTES,
                'OUT_BYTES':el.OUT_BYTES,
                'IN_PKTS':el.IN_PKTS,
                'OUT_PKTS':el.OUT_PKTS,
                'TCP_FLAGS':el.TCP_FLAGS,
                'FLOW_DURATION_MILLISECONDS':el.FLOW_DURATION_MILLISECONDS,
            }
            return JsonResponse(data, status = 200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error':'Something went wrong'}, status = 405)