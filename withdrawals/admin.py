from django.contrib import admin
from .models import Withdrawal


@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'amount',
        'wallet_address',
        'status',
        'pay30_confirmed',
        'pay30_display',
        'created_at',
    )
    
    list_filter = ('status', 'pay30_confirmed')
    actions = ['confirm_30_percent']

    def pay30_display(self, obj):
        """Display 30% amount nicely in admin list"""
        amount = obj.pay30_amount()
        return f"${amount:,.2f}"
    
    pay30_display.short_description = "30% Amount"

    @admin.action(description="Confirm 30% upfront payment for selected withdrawals")
    def confirm_30_percent(self, request, queryset):
        updated = 0
        for withdrawal in queryset:
            if not withdrawal.pay30_confirmed:
                withdrawal.pay30_confirmed = True
                
                # Deduct 30% from user's balance
                withdrawal.user.balance -= withdrawal.pay30_amount()
                withdrawal.user.save()
                
                withdrawal.save()
                updated += 1
                
        self.message_user(request, f"Successfully confirmed 30% payment for {updated} withdrawal(s).")