from django.shortcuts import render, redirect
from .forms import SizeRecommendationForm
from .utils import recommend_size
from django.http import HttpResponse  # HttpResponse 추가

def recommendation(request):
    if request.method == 'POST':
        # form을 직접 생성하지 않고, POST 데이터를 사용하지 않는다.
        # form = SizeRecommendationForm(request.POST)

        # POST 데이터에서 필요한 값을 직접 추출
        size_differences = diff(request)
        
        test1 = request.session.get('predict_shoulder', 0)
        test2 = request.session.get('Cshoulder', 0)
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
        clothes_sizes = {
            'shoulder': request.session.get('shoulder', 0),
            'chest': request.session.get('chest', 0),
            'total_length': request.session.get('total_length', 0),
            'sleeve': request.session.get('sleeve', 0),
            'waist': request.session.get('waist', 0),
            'hip': request.session.get('hip', 0),
            'bottom_length': request.session.get('bottom_length', 0),
            'thighs': request.session.get('thigh', 0),
    }
        for size_name, predicted_size in predicted_sizes.items():
            print(f"Predicted {size_name}: {predicted_size}")

        for size_name, clothes_size in clothes_sizes.items():
            print(f"Clothes {size_name}: {clothes_size}")


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
        # 폼을 생성하는 부분 생략
        # form = SizeRecommendationForm()

        # 폼이 필요하지 않은 경우 바로 결과값을 보여줌
        return render(request, 'recommendation/result.html', {'form': None})