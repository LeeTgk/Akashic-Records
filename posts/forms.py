from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_text = forms.CharField(label='Texto gerador', disabled=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    generated_text = forms.CharField(label='Texto gerado', disabled=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    class Meta:
        model = Post
        exclude = ['post_id', 'created_by', 'created_at', 'updated_at']
