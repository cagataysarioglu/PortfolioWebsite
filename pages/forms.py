from django import forms
from pages.models import Contact
from django.utils.translation import gettext as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['namesurname', 'email', 'subject', 'image', 'message']
        widgets = {
            'namesurname': forms.TextInput(attrs={'placeholder': _('Ad ve soyad'), 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': _('e-Posta adresi'), 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': _('Konu'), 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'placeholder': _('Görsel (İsteğe bağlı)'), 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': _('İleti'), 'class': 'form-control'}),
        }
