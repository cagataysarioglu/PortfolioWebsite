from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ürün Adı")
    amount = models.CharField(max_length=50, verbose_name="Ürün Adedi")
    price = models.IntegerField(blank=True, null=True, verbose_name="Ürün Fiyatı")
    image = models.ImageField(blank=True, null=True, verbose_name="Ürün Görseli")
    description = models.TextField(blank=True, null=True, verbose_name="Ürün Açıklaması")
    is_published = models.BooleanField(default=True, verbose_name='Yayında mı?')

    def __str__(self):
        return self.name

    def getImagePath(self):
        return '/img/' + str(self.image)
