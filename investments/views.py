from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Investment
from decimal import Decimal

@login_required
def invest_view(request):
    message = None
    user = request.user

    # 🔥 ADD THIS
    plans = [
        ('3M', '3 Months', 20),
        ('6M', '6 Months', 50),
        ('1Y', '1 Year', 100),
    ]


    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        plan = request.POST.get('plan')

        if amount > user.balance:
            message = 'Insufficient balance'
        else:
            user.balance -= amount

            multiplier = {
                '3M': Decimal('1.2'),   # +20%
                '6M': Decimal('1.5'),   # +50%
                '1Y': Decimal('2.0'),   # +100%
            }

            profit = amount * multiplier.get(plan, Decimal('1'))

            Investment.objects.create(
                user=user,
                amount=amount,
                plan=plan,
                profit=profit
            )

            user.save()
            message = f'Investment successful! Expected return: ${profit:.2f}'

    return render(request, 'invest.html', {  
        'balance': user.balance,
        'message': message,
        'plans': plans  
    })