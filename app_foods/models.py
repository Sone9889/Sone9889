
from django.db import models

# Create your models here.

class Food(models.Model):
    titel = models.CharField(max_length=60)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=True)
    promotion_end_at = models.DateTimeField(null=True, blank=True)
    desciption = models.TextField(null=True, blank=True)
    image_relative_url = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self) -> str:
        return '{} (id={})'.format(self.titel, self.id)