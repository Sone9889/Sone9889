from django.db import models

# Create your models here.

class Subscription(models.Model):
    STATUS = [
         ('unapproved', 'Unapproved'),
         ('anapproved', 'Anapproved'),
         ('banned', 'Banned')

    ]

    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    status = models.CharField(max_length=15, choices=STATUS, default='unapproved')
    registerd_at = models.DateTimeField(auto_now_add=True)
    food_set = models.ManyToManyField('app_foods.Food')

    def __str__(self) -> str:
        return '{} (id={})'.format(self.name, self.id)