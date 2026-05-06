from django import forms
from .models import Book1  

class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter book title',
            'class': "form-control", 
            'id': 'jsID'
        })
    )
    
    author = forms.CharField(
        max_length=100,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter author name',
            'class': "form-control"
        })
    )

    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': "form-control",
            'step': '0.01'
        })
    )

    edition = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': "form-control"
        })
    )

    class Meta:
        model = Book1 
        fields = ['title', 'author', 'price', 'edition']