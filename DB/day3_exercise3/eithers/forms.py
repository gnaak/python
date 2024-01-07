from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'issue_a': 'RED TEAM',
            'issue_b': 'BLUE TEAM',
        }
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('pick','content',)

	
class CommentForm(forms.ModelForm):
    PICK_A = False
    PICK_B = True
    PICKS = [
        (PICK_A, 'RED TEAM'),
        (PICK_B, 'BLUE TEAM'),
    ]
    pick = forms.ChoiceField(choices=PICKS, widget=forms.Select())

    class Meta:
        model = Comment
        fields = ['pick', 'content']