# models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()

#---------------------------------------------------------------------

# forms.py 생성 - Form
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length = 100)
    content = forms.CharField(widget = forms.Textarea)

#---------------------------------------------------------------------

# forms.py 생성 - ModelForm
from django import forms
from .modles import Article

class ArticleForm(forms.ModelForm):
    class Meta :
        model = Article
        fields = '__all__'
