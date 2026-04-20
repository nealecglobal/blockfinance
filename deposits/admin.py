from django.contrib import admin
from .models import Deposit, SupportRequest

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'coin', 'status', 'created_at')
    list_filter = ('status', 'coin')
    actions = ['confirm_deposit']
    search_fields = ('user__username', 'coin')

    def confirm_deposit(self, request, queryset):
        for deposit in queryset:
            if deposit.status != 'confirmed':
                deposit.status = 'confirmed'
                deposit.user.balance += deposit.amount
                deposit.user.save()
                deposit.save()
        self.message_user(request, "Selected deposits confirmed and balance updated.")
    confirm_deposit.short_description = "Confirm selected deposits"
    
@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'tx_hash', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('tx_hash', 'user__username')

    readonly_fields = ('user', 'tx_hash', 'message', 'screenshot', 'created_at')