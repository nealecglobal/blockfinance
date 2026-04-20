from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Withdrawal

@login_required
def withdraw_request(request):
    message = None
    user = request.user

    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        wallet_address = request.POST.get('wallet_address')

        if amount > user.balance:
            message = "Insufficient balance"
        else:
            pay_now = amount * Decimal('0.3')
            # Store in session for display
            request.session['withdraw_amount'] = str(amount)
            request.session['withdraw_wallet'] = wallet_address
            request.session['withdraw_pay_now'] = str(pay_now)
            return redirect('withdraw_pay')

    return render(request, 'withdraw_request.html', {'balance': user.balance, 'message': message})


@login_required
def withdraw_pay(request):
    amount = Decimal(request.session.get('withdraw_amount', '0'))
    wallet_address = request.session.get('withdraw_wallet', '')
    pay_now = Decimal(request.session.get('withdraw_pay_now', '0'))

    if request.method == 'POST':
        # Create Withdrawal record as pending, admin must confirm
        Withdrawal.objects.create(
            user=request.user,
            amount=amount,
            wallet_address=wallet_address,
            pay30_confirmed=False,
            status='pending'
        )

        # Clear session
        request.session.pop('withdraw_amount', None)
        request.session.pop('withdraw_wallet', None)
        request.session.pop('withdraw_pay_now', None)

        return render(request, 'withdraw_complete.html', {
            'amount': amount,
            'wallet_address': wallet_address,
            'pay_now': pay_now
        })

    return render(request, 'withdraw_pay.html', {
        'amount': amount,
        'wallet_address': wallet_address,
        'pay_now': pay_now
    })