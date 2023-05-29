from django import forms

from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields = ('category', 'name', 'description', 'author', 'image', )
        



