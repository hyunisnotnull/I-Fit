from django.shortcuts import render, redirect
from .utils import recommend_size, diff, determine_fit_info

def recommendation(request):
        size_differences = diff(request)

        # 예측된 크기와 사용자의 옷 크기 가져오기
        predicted_sizes = {
            'shoulder': round(request.session.get('predict_shoulder', 0), 2),
            'chest': round(request.session.get('predict_chest', 0), 2),
            'total_length': round(request.session.get('predict_top', 0), 2),
            'sleeve': round(request.session.get('predict_arm', 0), 2),
            'l_shoulder': round(request.session.get('predict_shoulder', 0), 2),
            'l_chest': round(request.session.get('predict_chest', 0), 2),
            'l_sleeve': round(request.session.get('predict_arm', 0), 2),
            's_shoulder': round(request.session.get('predict_shoulder', 0), 2),
            's_chest': round(request.session.get('predict_chest', 0), 2),
            's_total_length': round(request.session.get('predict_top', 0), 2),
            's_sleeve': round(request.session.get('predict_arm', 0), 2),
            'ntk' : round(request.session.get('predict_ntk', 0), 2) ,
            'neck' : round(request.session.get('predict_neck', 0), 2) ,
            'waist': round(request.session.get('predict_waist', 0), 2),
            'hip': round(request.session.get('predict_ass', 0), 2),
            'bottom_length': round(request.session.get('predict_bottom', 0), 2),
            'thighs': round(request.session.get('predict_thighs', 0), 2),
            }

        clothes_sizes = {
            'shoulder': round(request.session.get('shoulder', 0), 2),
            'chest': round(request.session.get('chest', 0), 2),
            'total_length': round(request.session.get('total_length', 0), 2),
            'sleeve': round(request.session.get('sleeve', 0), 2),
            'l_shoulder': round(request.session.get('l_shoulder', 0), 2),
            'l_chest': round(request.session.get('l_chest', 0), 2),
            'l_sleeve': round(request.session.get('l_sleeve', 0), 2),
            's_shoulder': round(request.session.get('s_shoulder', 0), 2),
            's_chest': round(request.session.get('s_chest', 0), 2),
            's_total_length': round(request.session.get('s_total_length', 0), 2),
            's_sleeve': round(request.session.get('s_sleeve', 0), 2),
            'ntk': round(request.session.get('ntk', 0), 2),
            'neck': round(request.session.get('neck', 0), 2),
            'waist': round(request.session.get('waist', 0), 2),
            'hip': round(request.session.get('hip', 0), 2),
            'bottom_length': round(request.session.get('bottom_length', 0), 2),
            'thighs': round(request.session.get('thighs', 0), 2),
        }
        # 추천 사이즈 계산
        recommended_sizes = recommend_size(request)
        fit_info = determine_fit_info(size_differences)
        # HTML에 표시될 형식으로 크기 포맷팅
        formatted_sizes = {key: "{:.2f}".format(float(value)) for key, value in recommended_sizes.items()}
        # 결과 데이터 생성
        result_data = {
            'size_differences': size_differences,
            'predicted_sizes': predicted_sizes,
            'clothes_sizes': clothes_sizes,
            'recommended_sizes': formatted_sizes,
            'fit_info': fit_info,
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
            template_name = 'recommendation/result.html'


        # 결과 데이터를 템플릿에 전달하고 렌더링
        return render(request, template_name, result_data)