from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from pages.forms import ContactForm
from django.contrib import messages
from .models import Carousel

def index(request):
    photos = Carousel.objects.order_by('photo')
    context = {
        'photos': photos
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse('Geçersizlik söz konusu!')
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

def kvkk(request):
    return render(request, "pages/kvkk.html")

def selectLanguage(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
