from django.shortcuts import render, redirect
from .utils import recommend_size, diff

def recommendation(request):
    # 사용자 입력과 예측된 크기 사이의 차이 계산
    size_differences = diff(request)

    # 예측된 크기와 사용자의 옷 크기 가져오기
    predicted_sizes = {
        'shoulder': request.session.get('predict_shoulder', 0),
        'chest': request.session.get('predict_chest', 0),
        'total_length': request.session.get('predict_top', 0),
        'sleeve': request.session.get('predict_arm', 0),
        'neck': request.session.get('predict_neck', 0),
        'ntk': request.session.get('predict_ntk', 0),
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
        'neck': request.session.get('neck', 0),
        'waist': request.session.get('waist', 0),
        'hip': request.session.get('hip', 0),
        'bottom_length': request.session.get('bottom_length', 0),
        'thighs': request.session.get('thigh', 0),
    }

    # 사용자에게 표시할 크기 차이와 추천된 크기 계산
    recommended_sizes = recommend_size(request)

    # HTML에 표시될 형식으로 크기 포맷팅
    formatted_sizes = {key: "{:.2f}".format(float(value)) for key, value in recommended_sizes.items()}

    # 결과 데이터 생성
    result_data = {
        'size_differences': size_differences,
        'predicted_sizes': predicted_sizes,
        'clothes_sizes': clothes_sizes,
        'recommended_sizes': formatted_sizes,
    }

    # 중간 결과 확인
    print("Result Data:", result_data)

    # 의류 타입에 따라 다른 템플릿 선택
    clothing_type = request.session.get('clothing_type')
    if clothing_type in ['top', 'outer']:
        template_name = 'recommendation/top_result.html'
    elif clothing_type in ['bottom', 'skirt']:
        template_name = 'recommendation/bottom_result.html'
    elif clothing_type == 'long':
        template_name = 'recommendation/long_result.html'
    elif clothing_type == 'shirt':
        template_name = 'recommendation/shirt_result.html'
    else:
        # 추후 추가할 의류 타입이 있다면 여기에 추가
        template_name = 'recommendation/default_result.html'

    # 결과 데이터를 템플릿에 전달하고 렌더링
    return render(request, template_name, result_data)
