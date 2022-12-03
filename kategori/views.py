from django.http import HttpResponseRedirect
from kategori.models import Kategori
from kategori.forms import KategoriForm
from django.http.response import HttpResponse
from kategori.models import Kategori
from users.views import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def index(request):
    kategoris = Kategori.objects.filter(user=request.user)
    response = {'kategoris': kategoris}
    return render(request, 'kategori_index.html', response)

@login_required(login_url='/login/')
@user_passes_test(check_role_pencatat)
def buat_kategori(request):
    context = {}
  
    form = KategoriForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        kategori_form = form.save(commit=False)
        kategori_form.user = request.user
        kategori_form.save()
        return HttpResponseRedirect(reverse('kategori:index'))
    
    context['form']= form
    return render(request, "buat_kategori.html", context)