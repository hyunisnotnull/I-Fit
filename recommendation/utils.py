def recommend_size(request):
    size_keys = [
        ('shoulder', 'recommended_size_shoulder'),
        ('chest', 'recommended_size_chest'),
        ('total_length', 'recommended_size_total_length'),
        ('sleeve', 'recommended_size_sleeve'),
        ('waist', 'recommended_size_waist'),
        ('hip', 'recommended_size_hip'),
        ('bottom_length', 'recommended_size_bottom_length'),
        ('thigh', 'recommended_size_thigh'),
    ]

    for size_key, recommended_key in size_keys:
        diff_size = request.session.get(f'diff_{size_key}', 0)
        request.session[recommended_key] = diff_size

    recommended_sizes = {recommended_key: request.session[recommended_key] for _, recommended_key in size_keys}
    return recommended_sizes

def diff(request):
    # 예측된 사용자 신체 사이즈 가져오기
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
    

    # 입력된 옷 사이즈 가져오기
    clothing_type = request.session.get('clothing_type')
    clothes_sizes = {
        'shoulder': request.session.get('clothes_shoulder', 0),
        'chest': request.session.get('clothes_chest', 0),
        'total_length': request.session.get('clothes_total_length', 0),
        'sleeve': request.session.get('clothes_sleeve', 0),
        'waist': request.session.get('clothes_waist', 0),
        'hip': request.session.get('clothes_hip', 0),
        'bottom_length': request.session.get('clothes_bottom_length', 0),
        'thighs': request.session.get('clothes_thigh', 0),
    }

    # 차이 계산 및 세션에 저장
    differences = {}
    for size_name in predicted_sizes.keys():
        predicted_size = predicted_sizes[size_name]
        clothes_size = clothes_sizes.get(size_name, 0)
        differences[size_name] = abs(predicted_size - clothes_size)
        request.session[f'diff_{size_name}'] = differences[size_name]

    return differences
