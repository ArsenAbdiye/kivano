from django.db import models

class Advertising(models.Model):
    advertising_image = models.ImageField('изображение рекламы', upload_to='advertising')
    image_link = models.CharField('ссылка рекламы', max_length=255)
    order = models.PositiveIntegerField("Порядок", default=1)

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
        ordering = ("order",)

    def __str__(self):
        return  'реклама ' + str(self.order)



class PlatformLink(models.Model):
    platform_image = models.ImageField('иконка платформы', upload_to='platformLinks')
    platform_link = models.CharField('ссылка платформы', max_length=255)
    platform_name = models.CharField('название платформы', max_length=50)
    is_socialnetwork = models.BooleanField('Это социальная сеть?', default=True)
    class Meta:
        verbose_name = "Платформа"
        verbose_name_plural = "Платформы"

    def __str__(self):
        return self.platform_name
    

class Contact(models.Model):
    phone_number = models.CharField('Номер телефона', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    contact_image = models.ImageField('Иконка контакта', null=True, blank=True)
    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактные данные"

    def __str__(self):
        return f"{self.phone_number or self.email}"
