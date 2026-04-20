from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Deposit(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]

    COIN_CHOICES = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('BNB', 'BNB'),
        ('SOL', 'Solana'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    coin = models.CharField(
        max_length=10,
        choices=COIN_CHOICES,
        default='BTC'
    )

    crypto_address = models.CharField(max_length=100)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.coin} - {self.amount} - {self.status}"
    
from django.db import models
from django.conf import settings


class SupportRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tx_hash = models.CharField(max_length=200)
    screenshot = models.ImageField(upload_to='support/')
    message = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        default='pending',
        choices=[
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('rejected', 'Rejected'),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tx_hash}"