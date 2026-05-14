from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Category

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Имэйл'}))
    first_name = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Нэр'}))
    last_name = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Овог'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Нэвтрэх нэр'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Нэвтрэх нэр 50 тэмдэгтээс бага байх ёстой.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Нууц үг'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Нууц үг 8 тэмдэгтээс багагүй байх ёстой.</small></span>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Нууц үг давтах'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Нууц үгийг дахин оруулна уу.</small></span>'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Бүтээгдэхүүний нэр'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Тайлбар...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }
        labels = {
            'name': 'Нэр',
            'price': 'Үнэ (₮)',
            'category': 'Ангилал',
            'description': 'Тайлбар',
            'image': 'Зураг',
            'is_sale': 'Хямдралтай эсэх',
            'sale_price': 'Хямдрал үнэ (₮)',
        }
