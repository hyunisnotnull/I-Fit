from django.shortcuts import render
from .utils import recommend_size, diff 
from .forms import SizeRecommendationForm
# Create your views here.
import logging

def recommendation(request):
    if request.method == 'POST':
        form = SizeRecommendationForm(request.POST)

        # 옷 사이즈 차이 계산
        size_differences = diff(request)

        # 추천 사이즈 계산
        recommended_sizes = recommend_size(request)

        result_data = {
            'diff_shoulder': size_differences.get('diff_shoulder', 0),
            'diff_chest': size_differences.get('diff_chest', 0),
            'diff_total_length': size_differences.get('diff_total_length', 0),
            'diff_sleeve': size_differences.get('diff_sleeve', 0),
            'diff_waist': size_differences.get('diff_waist', 0),
            'diff_hip': size_differences.get('diff_hip', 0),
            'diff_bottom_length': size_differences.get('diff_bottom_length', 0),
            'diff_thigh': size_differences.get('diff_thigh', 0),
            'recommended_size_shoulder': recommended_sizes.get('recommended_size_shoulder', 0),
            'recommended_size_chest': recommended_sizes.get('recommended_size_chest', 0),
            'recommended_size_total_length': recommended_sizes.get('recommended_size_total_length', 0),
            'recommended_size_sleeve': recommended_sizes.get('recommended_size_sleeve', 0),
            'recommended_size_waist': recommended_sizes.get('recommended_size_waist', 0),
            'recommended_size_hip': recommended_sizes.get('recommended_size_hip', 0),
            'recommended_size_bottom_length': recommended_sizes.get('recommended_size_bottom_length', 0),
            'recommended_size_thigh': recommended_sizes.get('recommended_size_thigh', 0),
            'size_differences': size_differences,
            'recommended_sizes': recommended_sizes,

        }

        return render(request, 'recommendation/result.html', result_data)

    else:
        form = SizeRecommendationForm()

    return render(request, 'recommendation/result.html', {'form': form})
