# forms.py
from django import forms

class ReviewForm(forms.Form):
    SIZE_CHOICES = [
        ('big', '크다'),
        ('small', '작다'),
        ('normal', '보통'),
    ]

    top = forms.ChoiceField(choices=SIZE_CHOICES, label='상의')
    bottom = forms.ChoiceField(choices=SIZE_CHOICES, label='하의')
    chest = forms.ChoiceField(choices=SIZE_CHOICES, label='가슴')
    shoulder = forms.ChoiceField(choices=SIZE_CHOICES, label='어깨')
    arm = forms.ChoiceField(choices=SIZE_CHOICES, label='팔')
    neck = forms.ChoiceField(choices=SIZE_CHOICES, label='목')
    waist = forms.ChoiceField(choices=SIZE_CHOICES, label='허리')
    ass = forms.ChoiceField(choices=SIZE_CHOICES, label='엉덩이')
    thighs = forms.ChoiceField(choices=SIZE_CHOICES, label='허벅지')
