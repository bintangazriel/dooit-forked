from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Kategori
from .forms import KategoriForm
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
    list_kategori = Kategori.objects.all()
    response = {'list_kategori': list_kategori}
    return render(request, 'kategori.html', response)

def add_kategori(request):
    context ={}
    form = KategoriForm(request.POST or None)
    if form.is_valid():
        form.save()
        if request.method == 'POST':
            return HttpResponseRedirect("/kategori/add")
    context['form']= form
    return render(request, "add_kategori.html", context)