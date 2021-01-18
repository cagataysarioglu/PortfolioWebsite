from django.db import models

class Contact(models.Model):
    namesurname = models.CharField(max_length=30, verbose_name='Ad-Soyad')
    email = models.EmailField(verbose_name='e-Posta')
    subject = models.CharField(max_length=70, verbose_name='Konu')
    message = models.TextField(verbose_name='İleti')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')

class Carousel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Görsel Adı")
    photo = models.ImageField(blank=False, null=True, verbose_name="Fotoğraf")

    def __str__(self):
        return self.name

    def getPhotoPath(self):
        return '/img/' + str(self.photo)
