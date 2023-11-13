from django.shortcuts import render, redirect
from .forms import ClothingSizeInputForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def clothes(request):
    if request.method == 'POST':
        form = ClothingSizeInputForm(request.POST)

        print('insert clothes')
        print( request.session.get('user_height') )

        if form.is_valid():
            clothing_type = form.cleaned_data['clothing_type']
            # 선택한 옷의 종류에 따라 필요한 옷 치수 입력을 요구하거나 입력된 데이터를 처리합니다.
            if clothing_type in ['outer', 'top']:
                # 상의 및 아우터의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                # 이어서 데이터 처리 코드를 작성
            elif clothing_type in ['bottom', 'skirt']:
                # 바지 및 치마의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                waist = form.cleaned_data['waist']
                hip = form.cleaned_data['hip']
                bottom_length = form.cleaned_data['bottom_length']
                thigh = form.cleaned_data['thigh']
                # 이어서 데이터 처리 코드를 작성
            # 필요에 따라 딥러닝 모델로 데이터를 전달하고 추천 사이즈를 받는 코드를 작성
            return redirect('/recommendation')
    else:

        print('insert getclothes')
        print( request.session.get('user_height') )
        print( request.session.get('user_top') )
        print( request.session.get('user_chest') )
        print( request.session.get('user_arm') )
        print( request.session.get('user_height') )
        print( request.session.get('user_waist') )
        print( request.session.get('user_height') )

        form = ClothingSizeInputForm()
    return render(request, 'clothes/C_input.html', {'form': form})
