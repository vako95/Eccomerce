from django import forms
from ..models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ("created_at", "updated_at", "slug", "tag")
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'fullwidth-textarea',
                
                'placeholder': 'Describe the product'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': 0.01,
                'placeholder': 'Enter price'
            }),
            'poster': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'brand': forms.Select(attrs={
                'class': 'form-control',
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100,
                'placeholder': 'Enter discount percentage'
            }),
            'tax': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10000000,
                'placeholder': 'Enter tax'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["content"].widget.attrs['class'] = "fullwidth-textarea"
