# utils.py
def recommend_size(request):
    size_keys = [
        ('shoulder', 'recommended_size_shoulder'),
        ('chest', 'recommended_size_chest'),
        ('total_length', 'recommended_size_total_length'),
        ('sleeve', 'recommended_size_sleeve'),
        ('neck', 'recommended_size_neck'),
        ('ntk', 'recommended_size_ntk'),
        ('waist', 'recommended_size_waist'),
        ('hip', 'recommended_size_hip'),
        ('bottom_length', 'recommended_size_bottom_length'),
        ('thigh', 'recommended_size_thigh'),
    ]
    recommended_sizes = {key: request.session.get(value, 0) for key, value in size_keys}
    return recommended_sizes

def diff(request):
    # 예측된 사용자 신체 사이즈 가져오기
    predicted_sizes = {
        'shoulder': request.session.get('predict_shoulder', 0),
        'chest': request.session.get('predict_chest', 0),
        'total_length': request.session.get('predict_top', 0),
        'sleeve': request.session.get('predict_arm', 0),
        'ntk' : request.session.get('predict_ntk', 0),
        'neck' : request.session.get('predict_neck', 0),
        'waist': request.session.get('predict_waist', 0),
        'hip': request.session.get('predict_ass', 0),
        'bottom_length': request.session.get('predict_bottom', 0),
        'thighs': request.session.get('predict_thighs', 0),
        }
    
    # 입력된 옷 사이즈 가져오기
    clothing_type = request.session.get('clothing_type')
    clothes_sizes = {
        'shoulder': request.session.get('shoulder', 0),
        'chest': request.session.get('chest', 0),
        'ntk': request.session.get('total_length', 0),
        'total_length': request.session.get('total_length', 0),
        'neck': request.session.get('neck', 0),
        'sleeve': request.session.get('sleeve', 0),
        'waist': request.session.get('waist', 0),
        'hip': request.session.get('hip', 0),
        'bottom_length': request.session.get('bottom_length', 0),
        'thighs': request.session.get('thigh', 0),
    }

    # 차이 계산 및 세션에 저장
    differences = {}
    for size_name, predicted_size in predicted_sizes.items():
        clothes_size = clothes_sizes.get(size_name, 0)
        difference = predicted_size - clothes_size
        comparison = '작습니다' if difference > 0 else '큽니다' if difference < 0 else '같습니다'
        differences[size_name] = {
            'difference': abs(difference),
            'comparison': comparison
        }
        request.session[f'diff_{size_name}'] = differences[size_name]
  
    return differences

