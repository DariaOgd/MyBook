from django import forms

from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields = ('category', 'name', 'description', 'author', 'image', )
        



class EditBookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields = ( 'name', 'description', 'author', 'image', )
        



