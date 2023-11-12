from django.shortcuts import render
#from .recommendation import recommend_size  # 딥러닝 모델을 사용할 모듈
from .forms import SizeRecommendationForm
# Create your views here.
import logging

def recommendation(request):
    if request.method == 'POST':
        form = SizeRecommendationForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            clothing_type = form.cleaned_data['clothing_type']
            logging.warning('1.여기서 문제다.', height)

            additional_info = {}  # 옷 종류에 따른 추가 정보
            if clothing_type in ['outer', 'top']:
                additional_info['shoulder'] = form.cleaned_data['shoulder']
                additional_info['chest'] = form.cleaned_data['chest']
                additional_info['total_length'] = form.cleaned_data['total_length']
                additional_info['sleeve'] = form.cleaned_data['sleeve']
            elif clothing_type in ['bottom', 'skirt']:
                additional_info['waist'] = form.cleaned_data['waist']
                additional_info['hip'] = form.cleaned_data['hip']
                additional_info['bottom_length'] = form.cleaned_data['bottom_length']
                additional_info['thigh'] = form.cleaned_data['thigh']
            
            # 딥러닝 모델을 사용하여 사이즈 추천
           # recommended_size = recommend_size(gender, height, weight, clothing_type, additional_info)
            
            # 추천된 사이즈를 사용자에게 표시
           # return render(request, 'recommendation_result.html', {'recommended_size': recommended_size})
    else:
        form = SizeRecommendationForm()