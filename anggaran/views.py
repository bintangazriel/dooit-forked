from django.shortcuts import render
from django.http import HttpResponse
from anggaran.forms import AnggaranForm
from anggaran.models import Anggaran
from users.views import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def index(request):
    anggarans = Anggaran.objects.filter(user=request.user)
    response = {'anggarans': anggarans}
    return render(request, 'anggaran_index.html', response)

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def buat_anggaran(request):
    context = {}
  
    form = AnggaranForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        anggaran_form = form.save(commit=False)
        anggaran_form.user = request.user
        anggaran_form.save()
        return HttpResponseRedirect(reverse('anggaran:index'))
    
    context['form']= form
    return render(request, "buat_anggaran.html", context)
