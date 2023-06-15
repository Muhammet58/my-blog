from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']

        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(attrs={'class': 'form-control', 'maxlength': 100 }),
            'author': forms.Select(attrs={'class': 'selectpicker form-control', 'data-width': '200px'})
        }