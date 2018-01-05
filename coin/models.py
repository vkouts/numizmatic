from django.db import models
from country.models import Country


class Coin(models.Model):
    title = models.TextField('Наименование')
    year_from = models.IntegerField('Год начала чеканки', null=True, blank=True)
    year_to = models.IntegerField('Год конца чеканки', null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.CASCADE)
    material = models.ForeignKey('CoinMaterial', verbose_name='Материал монеты',
                                 on_delete=models.CASCADE, null=True, blank=True)
    circulation = models.IntegerField(verbose_name='Тираж', null=True, blank=True)

    def __str__(self):
        return self.title


class CoinImage(models.Model):
    IMAGE_AVERS = 'A'
    IMAGE_REVERS = 'B'
    IMAGE_GURT = 'C'
    IMAGE_OTHER = 'N'

    TYPES = (
        (IMAGE_AVERS, 'Avers'),
        (IMAGE_REVERS, 'Revers'),
        (IMAGE_GURT, 'Gurt'),
        (IMAGE_OTHER, 'Other')
    )

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coins/%Y/%m/%d/')
    type = models.CharField(max_length=1, choices=TYPES, default=IMAGE_OTHER)

    def __str__(self):
        return self.image.url


class CoinLink(models.Model):
    link = models.URLField()
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.coin.title, self.link)


class CoinMaterial(models.Model):
    title = models.CharField(max_length=512)

    def __str__(self):
        return self.title