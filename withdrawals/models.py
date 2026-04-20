from django.db import models
from django.conf import settings
from decimal import Decimal

User = settings.AUTH_USER_MODEL


class Withdrawal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    wallet_address = models.CharField(max_length=100)
    pay30_confirmed = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def pay30_amount(self):
        """Calculate 30% of the withdrawal amount"""
        return self.amount * Decimal('0.3')

    def __str__(self):
        return f"{self.user.username} - ${self.amount} - {self.status}"