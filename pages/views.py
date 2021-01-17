from django.shortcuts import render
from pages.forms import ContactForm
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'İletiniz başarıyla gönderildi.')
            messages.success(request, 'İletiniz başarıyla gönderildi.')
            form = ContactForm()
    else:
        # messages.add_message(request, messages.ERROR, 'İletiniz gönderilirken bir hata oluştu.')
        messages.error(request, 'İletiniz gönderilirken bir hata oluştu.')
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "pages/contact.html", context)
