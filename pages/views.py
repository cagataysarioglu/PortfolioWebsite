from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            try:
                form.save()
            except:
                return HttpResponse('Invalid header found.')
            messages.add_message(request, messages.SUCCESS, 'İletiniz başarıyla gönderildi.')
            # return redirect("contact")
            form = ContactForm()
    else:
        # messages.add_message(request, messages.ERROR, 'İletiniz gönderilirken bir hata oluştu.')
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "pages/contact.html", context)
