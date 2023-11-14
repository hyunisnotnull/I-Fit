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
        
        test1 = request.session.get('predict_shoulder', 0)
        test2 = request.session.get('clothes_shoulder', 0)
        print(f"predict: {test1}")
        print(f"clothes: {test2}")
        
        predicted_sizes = {
            'shoulder': request.session.get('predict_shoulder', 0),
            'chest': request.session.get('predict_chest', 0),
            'total_length': request.session.get('predict_top', 0),
            'sleeve': request.session.get('predict_arm', 0),
            'waist': request.session.get('predict_waist', 0),
            'hip': request.session.get('predict_ass', 0),
            'bottom_length': request.session.get('predict_bottom', 0),
            'thighs': request.session.get('predict_thighs', 0),
        }

        for size_name, predicted_size in predicted_sizes.items():
            print(f"Predicted {size_name}: {predicted_size}")

        # 추천 사이즈 계산
        recommended_sizes = recommend_size(request)

        result_data = {

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
            'predicted_sizes': predicted_sizes,

        }

        return render(request, 'recommendation/result.html', result_data)

    else:
        form = SizeRecommendationForm()

    return render(request, 'recommendation/result.html', {'form': form})
