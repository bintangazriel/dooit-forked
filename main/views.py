from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 1:
            return redirect('catatan-transaksi/view')
        else:
            return redirect('konsultan/dashboard')   
    return render(request, 'landing_page.html')