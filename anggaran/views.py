from django.shortcuts import render
from django.http import HttpResponse
from anggaran.forms import AnggaranForm
from anggaran.models import Anggaran


# Create your views here.
def index(request):
    # anggarans = Anggaran.objects.filter(user=request.user)
    anggarans = Anggaran.objects.all().values()
    response = {'anggarans': anggarans}
    return render(request, 'anggaran_index.html', response)

def buat_anggaran(request):
    context = {}
  
    form = AnggaranForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        anggaran_form = form.save(commit=False)
        # anggaran_form.user = request.user
        return HttpResponseRedirect(reverse('anggaran:index'))
    
    context['form']= form
    return render(request, "buat_anggaran.html", context)
