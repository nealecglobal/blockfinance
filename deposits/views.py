from django.shortcuts import render 
from django.contrib.auth.decorators import login_required 
from .models import Deposit, SupportRequest

@login_required
def deposit_view(request):

    btc_address = "bc1peq477ykl9a7qzups68pe3558690hzlek7vkc3m9ts2lwd29jgvmqsq9876"
    eth_address = "0x09660579f617cf3fda3df6243c8d12213ce178af"
    bnb_address = "0x09660579f617cf3fda3df6243c8d12213ce178af"
    sol_address = "8WFy31SwjdM6Y3aewjUnCPR5MQHUB2aq2GmN9wjFS5wo"

    if request.method == 'POST':

        amount = request.POST.get('amount')
        coin = request.POST.get('coin')

        if not amount:
            return render(request, 'deposit.html', {'error': 'Amount is required'})

        try:
            amount = float(amount)
        except:
            return render(request, 'deposit.html', {'error': 'Invalid amount'})

        if coin == "BTC":
            address = btc_address
        elif coin == "ETH":
            address = eth_address
        elif coin == "BNB":
            address = bnb_address
        else:
            address = sol_address

        Deposit.objects.create(
            user=request.user,
            amount=amount,
            coin=coin,
            crypto_address=address
        )

        return render(request, 'deposit.html', {
            'success': 'Deposit request submitted',
            'btc_address': btc_address,
            'eth_address': eth_address,
            'bnb_address': bnb_address,
            'sol_address': sol_address,
        })

    return render(request, 'deposit.html', {
        'btc_address': btc_address,
        'eth_address': eth_address,
        'bnb_address': bnb_address,
        'sol_address': sol_address,
    })
    
@login_required
def contact_view(request):

    if request.method == 'POST':

        tx_hash = request.POST.get('tx_hash')
        message = request.POST.get('message')
        screenshot = request.FILES.get('screenshot')

        if not tx_hash:
            return render(request, 'contact.html', {
                'error': 'Transaction hash is required'
            })

        SupportRequest.objects.create(
            user=request.user,
            tx_hash=tx_hash,
            message=message,
            screenshot=screenshot
        )

        return render(request, 'contact.html', {
            'success': 'Support request submitted successfully'
        })

    return render(request, 'contact.html')