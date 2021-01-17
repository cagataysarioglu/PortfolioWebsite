from django import forms
from pages.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['namesurname', 'email', 'subject', 'message']
        widgets = {
            'namesurname': forms.TextInput(attrs={'placeholder': 'Ad ve soyad', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e-Posta adresi', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'İleti', 'class': 'form-control'}),
        }
