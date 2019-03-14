from django import forms
from .models import Articles
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['body','slug']
        widgets={
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('May not be "Create"')
        return new_slug
        