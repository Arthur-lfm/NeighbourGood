from django import forms
from .models import Poll, Choice


class PollAddForm(forms.ModelForm):

    # mettre choice1 a "Rent" et choice2 a "Cancel" par defaut
    choice1 = forms.CharField(label='Choice 1', max_length=100, initial='Rent')
    choice2 = forms.CharField(label='Choice 2', max_length=100, initial='Cancel')

    class Meta:
        model = Poll
        fields = ['description', 'choice1', 'choice2']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 20}),
        }


class EditPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['description', ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class ChoiceAddForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_description', ]
        widgets = {
            'choice_description': forms.TextInput(attrs={'class': 'form-control', })
        }
