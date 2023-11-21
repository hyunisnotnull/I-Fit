from django.shortcuts import render, redirect
from .forms import ClothingSizeInputForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def clothes(request):
    if request.method == 'POST':
        form = ClothingSizeInputForm(request.POST)
        # 세션 초기화
        request.session['shoulder'] = 0
        request.session['chest'] = 0
        request.session['total_length'] = 0
        request.session['sleeve'] = 0
        request.session['l_shoulder'] = 0
        request.session['l_chest'] = 0
        request.session['l_sleeve'] = 0
        request.session['s_shoulder'] = 0
        request.session['s_chest'] = 0
        request.session['s_total_length'] = 0
        request.session['s_sleeve'] = 0
        request.session['ntk'] = 0
        request.session['neck'] = 0
        request.session['waist'] = 0
        request.session['hip'] = 0
        request.session['bottom_length'] = 0
        request.session['thighs'] = 0

        if form.is_valid():
            clothing_type = form.cleaned_data['clothing_type']
            request.session['clothing_type'] = clothing_type
            # 선택한 옷의 종류에 따라 필요한 옷 치수 입력을 요구하거나 입력된 데이터를 처리합니다.
            if clothing_type in ['outer', 'top']:
                # 상의 및 아우터의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                # 이어서 데이터 처리 코드를 작성
                # 데이터 저장 추가
                request.session['shoulder'] = shoulder
                request.session['chest'] = chest * 2
                request.session['total_length'] = total_length
                request.session['sleeve'] = sleeve

            elif clothing_type in ['bottom', 'skirt']:
                # 바지 및 치마의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                waist = form.cleaned_data['waist']
                hip = form.cleaned_data['hip']
                bottom_length = form.cleaned_data['bottom_length']
                thighs = form.cleaned_data['thighs']

                request.session['waist'] = waist * 2
                request.session['hip'] = hip * 2
                request.session['bottom_length'] = bottom_length
                request.session['thighs'] = thighs * 2


            elif clothing_type in ['long']:

                l_shoulder = form.cleaned_data['l_shoulder']
                l_chest = form.cleaned_data['l_chest']
                ntk = form.cleaned_data['ntk']
                l_sleeve = form.cleaned_data['l_sleeve']

                request.session['l_shoulder'] = l_shoulder
                request.session['l_chest'] = l_chest * 2
                request.session['ntk'] = ntk
                request.session['l_sleeve'] = l_sleeve


            elif clothing_type in ['shirt']:
                s_shoulder = form.cleaned_data['s_shoulder']
                s_chest = form.cleaned_data['s_chest']
                s_total_length = form.cleaned_data['s_total_length']
                s_sleeve = form.cleaned_data['s_sleeve']
                neck = form.cleaned_data['neck']

                request.session['s_shoulder'] = s_shoulder
                request.session['s_chest'] = s_chest * 2
                request.session['s_total_length'] = s_total_length
                request.session['s_sleeve'] = s_sleeve
                request.session['neck'] = neck

            return redirect('/recommendation')
        print(f"Session data after recommend_size: {request.session}")
    else:

        form = ClothingSizeInputForm()
    return render(request, 'clothes/C_input.html', {'form': form})