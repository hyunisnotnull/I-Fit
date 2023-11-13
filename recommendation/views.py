from django.shortcuts import render
from .utils import recommend_size 
from .forms import SizeRecommendationForm
# Create your views here.
import logging

# 수정 필요 
# 폼 받지 않고 return redirect('/recommendation')으로 호출 받았을때 실행되게 변경 필요
def recommendation(request):
    if request.method == 'POST':
        form = SizeRecommendationForm(request.POST)
        
        predict_top = request.session.get('predict_top', 0)
        predict_chest = request.session.get('predict_chest', 0)
        predict_shoulder = request.session.get('predict_shoulder', 0)
        predict_arm = request.session.get('predict_arm', 0)
        predict_neck = request.session.get('predict_neck', 0)
        predict_ntk = request.session.get('predict_ntk', 0)
        predict_waist = request.session.get('predict_waist', 0)
        predict_ass = request.session.get('predict_ass', 0)
        predict_bottom = request.session.get('predict_bottom', 0)
        predict_thighs = request.session.get('predict_thighs', 0)
        clothing_type = request.session.get('clothing_type')
                    
            # 예측한 사용자 신체 치수 정보
            
        print(f"predict_top: {predict_top}")
        # 상의
        if clothing_type in ['outer', 'top']:

            clothes_shoulder = request.session.get('clothes_shoulder', 0)
            clothes_chest = request.session.get('clothes_chest', 0)
            clothes_total_length = request.session.get('clothes_total_length', 0)
            clothes_sleeve = request.session.get('clothes_sleeve', 0)

            diff_shoulder = abs(predict_shoulder - clothes_shoulder)
            diff_chest = abs(predict_chest - clothes_chest)
            diff_total_length = abs(predict_top - clothes_total_length)
            diff_sleeve = abs(predict_arm - clothes_sleeve)
            
            request.session['diff_shoulder'] = diff_shoulder
            request.session['diff_chest'] = diff_chest
            request.session['diff_total_length'] = diff_total_length
            request.session['diff_sleeve'] = diff_sleeve
                
        # 하의
        elif clothing_type in ['bottom', 'skirt']:

            clothes_waist = request.session.get('clothes_waist', 0)
            clothes_hip = request.session.get('clothes_hip', 0)
            clothes_bottom_length = request.session.get('clothes_bottom_length', 0)
            clothes_thigh = request.session.get('clothes_thigh', 0)
            
            diff_waist = abs(predict_waist - clothes_waist)
            diff_hip = abs(predict_ass - clothes_hip)
            diff_bottom_length = abs(predict_bottom - clothes_bottom_length)
            diff_thigh = abs(predict_thighs - clothes_thigh)
            
            request.session['diff_waist'] = diff_waist
            request.session['diff_hip'] = diff_hip
            request.session['diff_bottom_length'] = diff_bottom_length
            request.session['diff_thigh'] = diff_thigh
                    
        recommend_size(request)
        
        result_data = {
            'diff_shoulder': request.session.get('diff_shoulder'),
            'diff_chest': request.session.get('diff_chest'),
            'diff_total_length': request.session.get('diff_total_length'),
            'diff_sleeve': request.session.get('diff_sleeve'),
            'diff_waist': request.session.get('diff_waist'),
            'diff_hip': request.session.get('diff_hip'),
            'diff_bottom_length': request.session.get('diff_bottom_length'),
            'diff_thigh': request.session.get('diff_thigh'),
        }
        return render(request, 'recommendation/result.html', result_data)


    else:
        form = SizeRecommendationForm()
        
    return render(request, 'recommendation/result.html', {'form': form})
