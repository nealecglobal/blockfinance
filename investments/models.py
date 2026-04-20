from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Investment(models.Model):
    PLAN_CHOICES = [
        ('3M', '3 Months'),
        ('6M', '6 Months'),
        ('1Y', '1 Year'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.plan}"