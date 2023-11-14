from django import forms

class ClothingSizeInputForm(forms.Form):
    CLOTHING_CHOICES = [
        ('outer', '아우터'),
        ('top', '상의'),
        ('bottom', '바지'),
        ('skirt', '치마'),
    ]

    clothing_type = forms.ChoiceField(label='옷의 종류', choices=CLOTHING_CHOICES)
    
    # 모든 옷 치수 필드를 추가합니다. 초기에는 빈 필드로 시작합니다.
    shoulder = forms.DecimalField(label='어깨너비 (cm)', required=False)
    chest = forms.DecimalField(label='가슴단면 (cm)', required=False)
    total_length = forms.DecimalField(label='총장 (cm)', required=False)
    sleeve = forms.DecimalField(label='소매길이 (cm)', required=False)
    
    waist = forms.DecimalField(label='허리단면 (cm)', required=False)
    hip = forms.DecimalField(label='엉덩이단면 (cm)', required=False)
    bottom_length = forms.DecimalField(label='총장 (cm)', required=False)
    thigh = forms.DecimalField(label='허벅지단면 (cm)', required=False)