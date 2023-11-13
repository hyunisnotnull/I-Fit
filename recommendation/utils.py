# recommendation/recommendation.py
def recommend_size(request):
    diff_shoulder = request.session.get('diff_shoulder', 0)
    diff_chest = request.session.get('diff_chest', 0)
    diff_total_length = request.session.get('diff_total_length', 0)
    diff_sleeve = request.session.get('diff_sleeve', 0)

    diff_waist = request.session.get('diff_waist', 0)
    diff_hip = request.session.get('diff_hip', 0)
    diff_bottom_length = request.session.get('diff_bottom_length', 0)
    diff_thigh = request.session.get('diff_thigh', 0)

    # 추천 차이를 세션에 저장
    request.session['recommended_size_shoulder'] = diff_shoulder
    request.session['recommended_size_chest'] = diff_chest
    request.session['recommended_size_total_length'] = diff_total_length
    request.session['recommended_size_sleeve'] = diff_sleeve

    request.session['recommended_size_waist'] = diff_waist
    request.session['recommended_size_hip'] = diff_hip
    request.session['recommended_size_bottom_length'] = diff_bottom_length
    request.session['recommended_size_thigh'] = diff_thigh

    # 추천 차이를 반환
    return {
        'recommended_size_shoulder': diff_shoulder,
        'recommended_size_chest': diff_chest,
        'recommended_size_total_length': diff_total_length,
        'recommended_size_sleeve': diff_sleeve,
        'recommended_size_waist': diff_waist,
        'recommended_size_hip': diff_hip,
        'recommended_size_bottom_length': diff_bottom_length,
        'recommended_size_thigh': diff_thigh,
    }
