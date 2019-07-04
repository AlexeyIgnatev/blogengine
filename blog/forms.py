from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter slug'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug "{}" is already exist'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter slug'}),
            'body': forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter body'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control mt-2'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug
