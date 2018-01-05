from django.db import models
from coin.models import Coin, CoinImage


# Create your models here.
class MyCoin(models.Model):
    STATE = (
        ('UNC', 'UNC'),
        ('AUNC', 'AUNC'),
        ('XF', 'XF'),
        ('VF', 'VF'),
        ('F', 'F'),
        ('G', 'G')
    )
    coin = models.ForeignKey(Coin, verbose_name='Монета', on_delete=models.CASCADE)
    state = models.CharField('Состояние монеты', max_length=5, choices=STATE, null=True, blank=True)
    year = models.IntegerField('Год чеканки', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.coin.title


class MyCoinImage(models.Model):
    coin = models.ForeignKey(MyCoin, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mycoins/%Y/%m/%d/')
    type = models.CharField(max_length=1, choices=CoinImage.TYPES, default=CoinImage.IMAGE_OTHER)

    def __str__(self):
        return self.image.url