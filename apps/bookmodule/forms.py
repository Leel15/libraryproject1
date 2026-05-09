from django import forms
from .models import Book1 ,Address ,Student,Address2,Student2 ,BookGallery
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


class StudentForm(forms.ModelForm):
    name = forms.CharField(label="Student Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age", initial=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        empty_label="Select Address",
        label="Student Address",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Student
        fields = ['name', 'age', 'address'] 




class Student2Form(forms.ModelForm):
     
    name = forms.CharField(label="Student Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age", initial=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        label="Select Addresses",
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']



class BookGalleryForm(forms.ModelForm):
    class Meta:
        model = BookGallery 
        fields = ['title', 'picture'] 