from django import forms
from django.contrib.auth import get_user_model
from tests.models import Tests, Questions, Answers


class AddTestForm(forms.ModelForm):
    class Meta:
        model = Tests
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': ' form_post', 'placeholder': 'Название теста'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'Описание'}),
        }

class AddQuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'Image']
        labels = {
            'Image': 'Картинка'
        }
        widgets = {
            'question': forms.TextInput(attrs={'class': ' form_post', 'placeholder': 'Вопрос'}),
        }

class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['answer', 'flag']
        widgets = {
            'answer': forms.TextInput(attrs={'class': ' form_post', 'placeholder': 'Ответ'}),
            'flag': forms.BooleanField(),
        }