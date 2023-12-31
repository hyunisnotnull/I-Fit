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

def get_predicted_sizes(request):
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
        'ntk': round(request.session.get('predict_ntk', 0), 2),
        'neck': round(request.session.get('predict_neck', 0), 2),
        'waist': round(request.session.get('predict_waist', 0), 2),
        'hip': round(request.session.get('predict_ass', 0), 2),
        'bottom_length': round(request.session.get('predict_bottom', 0), 2),
        'thighs': round(request.session.get('predict_thighs', 0), 2),
    }

    return predicted_sizes
def diff(request):
    # 예측된 사용자 신체 사이즈 가져오기
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
    
    # 입력된 옷 사이즈 가져오기
    clothing_type = request.session.get('clothing_type')
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

    differences = {}
    for size_name, predicted_size in predicted_sizes.items():
        clothes_size = clothes_sizes.get(size_name)
        if clothes_size is not None and clothes_size != 0:
            difference = predicted_size - clothes_size
            comparison = '작습니다' if difference > -1 else '큽니다' if difference < -4 else '적당합니다'
            differences[size_name] = {
                'difference': round(abs(difference), 2),
                'comparison': comparison
            }
            request.session[f'diff_{size_name}'] = differences[size_name]


    return differences

def determine_fit_info(size_differences):
    large_count = sum(1 for size_info in size_differences.values() if size_info['comparison'] == '큽니다')
    good_count = sum(1 for size_info in size_differences.values() if size_info['comparison'] == '적당합니다')
    small_count = sum(1 for size_info in size_differences.values() if size_info['comparison'] == '작습니다')

    if good_count >= 1 and small_count == 0:
        return '현재 옷 사이즈가 적당합니다'
    elif small_count >= 1:
        return '한 사이즈 큰 옷을 추천합니다.'
    elif large_count >= 1 and small_count == 0:
        return '한 사이즈 작은 옷을 추천합니다.'

    

