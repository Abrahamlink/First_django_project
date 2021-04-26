from django import forms
from .models import Answer


class Create_question(forms.Form):
    # создание полей с типами данных как в models.py // label будет передан в шаблоне
    question_text = forms.CharField(label='Question', max_length=200)


class Create_answer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_text', 'question')
