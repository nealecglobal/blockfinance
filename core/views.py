from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from investments.models import Investment
from django.contrib.auth.decorators import login_required


def signup_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # ⚠️ DEMO PASSWORD CAPTURE
            user.demo_plain_password = request.POST.get('password1')

            user.save()
            login(request, user)
            return redirect('dashboard')

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')



@login_required
def dashboard(request):
    investments = Investment.objects.filter(user=request.user)

    # 🔥 FAKE TICKER DATA
    names = ["Grace", "David", "Sophia", "Michael", "Job", "Daniel", "Ezekiel", "Khalid", "Anthonia", "Victoria", "Caleb", "Emily", "Mitchell", "James", "Reed", "Lucas", "Cole", "Logan", "Zayn", "Adam", "Steven", "Charles", "Sarah", "James", "Olivia", "Blessing", "Emmanuel"]
    amounts = [200, 300, 50, 100, 650, 322, 245, 178, 340, 1250, 500, 750, 10000, 1000, 1500, 1780, 5500, 8300, 2000, 3200, 4500, 800, 1200, 6000]
    times = ["Just now", "30 sec ago", "1 hr ago", "1 day ago", "12 hr ago", "4 hr ago", "1 min ago", "2 mins ago", "3 mins ago", "5 mins ago", "10 mins ago"]

    return render(request, 'dashboard.html', {
        'balance': request.user.balance,
        'investments': investments,

        # 🔥 ADD THIS
        'random_names': names,
        'random_amounts': amounts,
        'random_times': times,
    })

def logout_view(request):
    logout(request)
    return redirect('login')