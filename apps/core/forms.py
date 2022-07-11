from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from apps.core.models import Comment


class LoginForm(forms.Form):

    NEW_CHOICES = (
        ('LR', 'new'),
        ('TR', 'lol')
    )

    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    go = forms.BooleanField()
    choice = forms.ChoiceField(choices=NEW_CHOICES)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['rating', 'body']