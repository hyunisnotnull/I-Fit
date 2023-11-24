from django.shortcuts import render, redirect
from .models import reviewsModel
from .forms import ReviewForm

def reviews(request):
    context = {}

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            # 사용자의 입력값을 받아옵니다.
            review_top = form.cleaned_data['top']
            review_bottom = form.cleaned_data['bottom']
            review_chest = form.cleaned_data['chest']
            review_shoulder = form.cleaned_data['shoulder']
            review_arm = form.cleaned_data['arm']
            review_neck = form.cleaned_data['neck']
            review_waist = form.cleaned_data['waist']
            review_ass = form.cleaned_data['ass']
            review_thighs = form.cleaned_data['thighs']

            # 예측된 값을 세션에서 받아옵니다.
            predict_top = request.session.get('predict_top', 0)  # 기본값은 0으로 설정
            predict_chest = request.session.get('predict_chest', 0)
            predict_shoulder = request.session.get('predict_shoulder', 0)
            predict_arm = request.session.get('predict_arm', 0)
            predict_neck = request.session.get('predict_neck', 0)
            predict_ntk = request.session.get('predict_ntk', 0)
            predict_waist = request.session.get('predict_waist', 0)
            predict_ass = request.session.get('predict_ass', 0)
            predict_bottom = request.session.get('predict_bottom', 0)
            predict_thighs = request.session.get('predict_thighs', 0)

            # 리뷰에 따라 예측값을 업데이트합니다.
            predict_top = update_prediction(predict_top, review_top)
            predict_bottom = update_prediction(predict_bottom, review_bottom)
            predict_chest = update_prediction(predict_chest, review_chest)
            predict_shoulder = update_prediction(predict_shoulder, review_shoulder)
            predict_arm = update_prediction(predict_arm, review_arm)
            predict_neck = update_prediction(predict_neck, review_neck)
            predict_waist = update_prediction(predict_waist, review_waist)
            predict_ass = update_prediction(predict_ass, review_ass)
            predict_thighs = update_prediction(predict_thighs, review_thighs)

            # 업데이트된 값을 세션에 저장합니다.
            request.session['predict_top'] = predict_top
            request.session['predict_chest'] = predict_chest
            request.session['predict_shoulder'] = predict_shoulder
            request.session['predict_arm'] = predict_arm
            request.session['predict_neck'] = predict_neck
            request.session['predict_ntk'] = predict_ntk
            request.session['predict_waist'] = predict_waist
            request.session['predict_ass'] = predict_ass
            request.session['predict_bottom'] = predict_bottom
            request.session['predict_thighs'] = predict_thighs

            # 리뷰 데이터를 디비에 저장합니다.
            mediate_data = {
                'Mediate_top': request.session.get('Mediate_top'),
                'Mediate_chest': request.session.get('Mediate_chest'),
                'Mediate_shoulder': request.session.get('Mediate_shoulder'),
                'Mediate_arm': request.session.get('Mediate_arm'),
                'Mediate_neck': request.session.get('Mediate_neck'),
                'Mediate_ntk': request.session.get('Mediate_ntk'),
                'Mediate_waist': request.session.get('Mediate_waist'),
                'Mediate_ass': request.session.get('Mediate_ass'),
                'Mediate_bottom': request.session.get('Mediate_bottom'),
                'Mediate_thighs': request.session.get('Mediate_thighs'),
            }
            mediate_model_instance = reviewsModel(**mediate_data)
            mediate_model_instance.save()
            
            context['error'] = '리뷰 감사합니다. 좀 더 정확한 사이즈 비교에 도움을 주셔서 감사합니다'
        else:
            context['error'] = '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.'
    else:
        form = ReviewForm()

    return render(request, 'reviews/reviews.html', {'form': form}, context)

def update_prediction(original_value, review):
    # 리뷰에 따라 예측값을 업데이트하는 함수입니다.
    if review == 'big':
        return original_value * 0.9
    elif review == 'small':
        return original_value * 1.1
    else:
        return original_value
