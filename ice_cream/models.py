from django.db import models
from django.utils import timezone


class IceCream(models.Model):
    CHOCOLATE = 'Chocolate'
    VANILLA = 'Vanilla'
    BASE_CHOICES = (
        (CHOCOLATE, 'Chocolate'),
        (VANILLA, 'Vanilla'),
    )
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    SEASONAL = 'Seasonal'
    DAY_CHOICES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (SEASONAL, 'Seasonal'),
    )
    flavor = models.CharField(max_length=255)
    base = models.CharField(max_length=255, choices=BASE_CHOICES, default=CHOCOLATE,)
    available = models.CharField(max_length=20, choices=DAY_CHOICES, default=DAILY,)
    featured = models.BooleanField(default=True)
    date_churned = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.flavor
